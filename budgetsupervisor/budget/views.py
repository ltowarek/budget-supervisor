import base64
import json
import logging
import os
from typing import Any, Dict, List

import OpenSSL.crypto
from budget.forms import (
    CreateConnectionForm,
    CreateTransactionForm,
    RefreshConnectionForm,
    ReportIncomeForm,
    UpdateAccountForm,
    UpdateTransactionForm,
)
from budget.models import Account, Category, Connection, Transaction
from budget.services import (
    create_initial_balance,
    get_income_report,
    import_saltedge_accounts,
    import_saltedge_connection,
    import_saltedge_transactions,
)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    FormMixin,
    FormView,
    UpdateView,
)
from OpenSSL.crypto import FILETYPE_PEM, X509, load_publickey, verify
from saltedge_wrapper.factory import (
    accounts_api,
    connect_sessions_api,
    connections_api,
    transactions_api,
)
from saltedge_wrapper.utils import (
    create_connect_session,
    get_accounts,
    get_connection,
    get_pending_transactions,
    get_transactions,
    refresh_connection_in_saltedge,
    remove_connection_from_saltedge,
)
from users.models import Profile

logger = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "budget/index.html"


class ConnectionsListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self) -> QuerySet:
        return Connection.objects.filter(user=self.request.user).order_by("provider")


class ConnectionCreate(LoginRequiredMixin, FormView):
    template_name = "budget/connection_create.html"
    form_class = CreateConnectionForm
    success_url = reverse_lazy("connections:connection_list")

    def form_valid(self, form: CreateConnectionForm) -> HttpResponseRedirect:
        redirect_url = self.request.build_absolute_uri(str(self.success_url))
        connect_url = create_connect_session(
            redirect_url,
            str(self.request.user.profile.external_id),
            connect_sessions_api(),
        )
        return redirect(connect_url)

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context


class ConnectionUpdate(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Connection
    fields: List[str] = []
    success_url = reverse_lazy("connections:connection_list")
    success_message = "Connection was updated successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user


class ConnectionRefresh(
    LoginRequiredMixin, UserPassesTestMixin, SingleObjectMixin, FormView,
):
    model = Connection
    template_name = "budget/connection_refresh.html"
    form_class = RefreshConnectionForm
    success_url = reverse_lazy("connections:connection_list")

    def get(
        self, request: HttpRequest, *args: str, **kwargs: Any
    ) -> HttpResponseRedirect:
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(
        self, request: HttpRequest, *args: str, **kwargs: Any
    ) -> HttpResponseRedirect:
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def form_valid(self, form: RefreshConnectionForm) -> HttpResponseRedirect:
        connection = self.get_object()
        redirect_url = self.request.build_absolute_uri(str(self.success_url))
        connect_url = refresh_connection_in_saltedge(
            redirect_url, str(connection.external_id), connect_sessions_api()
        )
        return redirect(connect_url)


class ConnectionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Connection
    success_url = reverse_lazy("connections:connection_list")
    success_message = "Connection was deleted successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        connection = self.get_object()
        remove_connection_from_saltedge(str(connection.external_id), connections_api())
        accounts = Account.objects.filter(connection=connection)
        accounts.update(external_id=None)
        for account in accounts:
            transactions = Transaction.objects.filter(account=account)
            transactions.update(external_id=None)

        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class AccountListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self) -> QuerySet:
        return Account.objects.filter(user=self.request.user).order_by("name")


class AccountCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Account
    fields = [
        "name",
        "alias",
        "account_type",
    ]
    success_url = reverse_lazy("accounts:account_list")
    success_message = "Account was created successfully"

    def form_valid(self, form: ModelForm) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdate(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Account
    form_class = UpdateAccountForm
    success_url = reverse_lazy("accounts:account_list")
    success_message = "Account was updated successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user


class AccountDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Account
    success_url = reverse_lazy("accounts:account_list")
    success_message = "Account was deleted successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class TransactionListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self) -> QuerySet:
        return Transaction.objects.filter(user=self.request.user).order_by("-date")


class TransactionCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Transaction
    form_class = CreateTransactionForm
    success_url = reverse_lazy("transactions:transaction_list")
    success_message = "Transaction was created successfully"

    def form_valid(self, form: ModelForm) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, *args: Any, **kwargs: Any) -> ModelForm:
        form = super().get_form(*args, **kwargs)
        form.fields["account"].queryset = Account.objects.filter(user=self.request.user)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form


class TransactionUpdate(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Transaction
    form_class = UpdateTransactionForm
    success_url = reverse_lazy("transactions:transaction_list")
    success_message = "Transaction was updated successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def get_form(self, *args: Any, **kwargs: Any) -> ModelForm:
        form = super().get_form(*args, **kwargs)
        form.fields["account"].queryset = Account.objects.filter(user=self.request.user)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form


class TransactionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy("transactions:transaction_list")
    success_message = "Transaction was deleted successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class CategoryListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self) -> QuerySet:
        return Category.objects.filter(user=self.request.user).order_by("name")


class CategoryCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("categories:category_list")
    success_message = "Category was created successfully"

    def form_valid(self, form: ModelForm) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdate(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("categories:category_list")
    success_message = "Category was updated successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user


class CategoryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("categories:category_list")
    success_message = "Category was deleted successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class ReportIncomeView(LoginRequiredMixin, FormMixin, TemplateView):
    template_name = "budget/report_income.html"
    form_class = ReportIncomeForm

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form_kwargs(self) -> Dict:
        kwargs = super().get_form_kwargs()
        if self.request.GET:
            kwargs["data"] = self.request.GET
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form: ReportIncomeForm) -> HttpResponse:
        report = get_income_report(
            form.cleaned_data["accounts"],
            form.cleaned_data["from_date"],
            form.cleaned_data["to_date"],
            form.cleaned_data["excluded_categories"],
        )
        return self.render_to_response(self.get_context_data(form=form, report=report))


def verify_saltedge_signature(request: HttpRequest) -> None:
    uri = request.build_absolute_uri(request.path)
    body = request.body.decode()
    data = f"{uri}|{body}"
    pem = os.environ["SALTEDGE_PUBLIC_KEY"]
    signature = request.headers["Signature"]
    verify_signature(pem, signature, data)


def verify_signature(pem: str, signature_base64: str, data: str) -> None:
    public_key = load_publickey(FILETYPE_PEM, pem)
    x509 = X509()
    x509.set_pubkey(public_key)
    signature = base64.b64decode(signature_base64)
    verify(x509, signature, data, "sha256")


@method_decorator(csrf_exempt, name="dispatch")
class CallbackSuccess(View):
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        logger.error(
            f"Success callback\nHeaders:\n{request.headers}\nBody:\n{request.body}"
        )

        try:
            verify_saltedge_signature(request)
        except OpenSSL.crypto.Error:
            return HttpResponse(status=401)

        data = json.loads(request.body)["data"]
        external_customer_id = data["customer_id"]
        external_connection_id = data["connection_id"]

        profile = Profile.objects.filter(external_id=int(external_customer_id)).first()
        if not profile:
            return HttpResponse(status=400)
        user = profile.user

        saltedge_connection = get_connection(external_connection_id, connections_api())
        _ = import_saltedge_connection(saltedge_connection, user)

        saltedge_accounts = get_accounts(external_connection_id, accounts_api())
        imported_account_tuples = import_saltedge_accounts(saltedge_accounts, user)

        for saltedge_account, imported_account_tuple in zip(
            saltedge_accounts, imported_account_tuples
        ):
            saltedge_transactions = get_transactions(
                external_connection_id, saltedge_account.id, transactions_api()
            )
            _ = import_saltedge_transactions(saltedge_transactions, user)
            account, is_created = imported_account_tuple
            if is_created:
                saltedge_pending_transactions = get_pending_transactions(
                    external_connection_id, saltedge_account.id, transactions_api()
                )
                all_saltedge_transactions = (
                    saltedge_transactions + saltedge_pending_transactions
                )
                _ = create_initial_balance(
                    account, saltedge_account, all_saltedge_transactions
                )

        return HttpResponse(status=204)


@method_decorator(csrf_exempt, name="dispatch")
class CallbackFail(View):
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        logger.error(
            f"Fail callback\nHeaders:\n{request.headers}\nBody:\n{request.body}"
        )

        try:
            verify_saltedge_signature(request)
        except OpenSSL.crypto.Error:
            return HttpResponse(status=401)

        data = json.loads(request.body)["data"]
        connection_id = data["connection_id"]
        error_class = data["error_class"]

        if error_class == "InvalidCredentials":
            accounts = get_accounts(connection_id, accounts_api())
            if not accounts:
                remove_connection_from_saltedge(connection_id, connections_api())

        return HttpResponse(status=204)


@method_decorator(csrf_exempt, name="dispatch")
class CallbackDestroy(View):
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        logger.error(
            f"Destroy callback\nHeaders:\n{request.headers}\nBody:\n{request.body}"
        )

        try:
            verify_saltedge_signature(request)
        except OpenSSL.crypto.Error:
            return HttpResponse(status=401)

        data = json.loads(request.body)["data"]
        external_customer_id = int(data["customer_id"])
        external_connection_id = int(data["connection_id"])

        profile = Profile.objects.filter(external_id=external_customer_id).first()
        if not profile:
            return HttpResponse(status=400)
        user = profile.user

        connection = Connection.objects.filter(
            user=user, external_id=external_connection_id
        ).first()
        if not connection:
            return HttpResponse(status=400)

        accounts = Account.objects.filter(connection=connection)
        accounts.update(external_id=None)
        for account in accounts:
            transactions = Transaction.objects.filter(account=account)
            transactions.update(external_id=None)
        connection.delete()

        return HttpResponse(status=204)


@method_decorator(csrf_exempt, name="dispatch")
class CallbackNotify(View):
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        logger.error(
            f"Notify callback\nHeaders:\n{request.headers}\nBody:\n{request.body}"
        )

        try:
            verify_saltedge_signature(request)
        except OpenSSL.crypto.Error:
            return HttpResponse(status=401)

        return HttpResponse(status=204)


@method_decorator(csrf_exempt, name="dispatch")
class CallbackService(View):
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        logger.error(
            f"Service callback\nHeaders:\n{request.headers}\nBody:\n{request.body}"
        )

        try:
            verify_saltedge_signature(request)
        except OpenSSL.crypto.Error:
            return HttpResponse(status=401)

        return HttpResponse(status=204)
