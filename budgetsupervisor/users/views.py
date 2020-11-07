from typing import Any, List

from budget.models import Account, Connection, Transaction
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from saltedge_wrapper.factory import customers_api
from users.forms import ProfileConnectForm, ProfileDisconnectForm, SignUpForm
from users.models import Profile, User
from users.services import create_customer_in_saltedge, remove_customer_from_saltedge
from users.tokens import user_tokenizer

from budgetsupervisor import settings


class SignUpView(CreateView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")

    def form_valid(self, form: SignUpForm) -> HttpResponseRedirect:
        response = super().form_valid(form)

        user = self.object
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        token = user_tokenizer.make_token(user)
        url = self.request.build_absolute_uri(
            str(reverse("activate", kwargs={"user_id": user_id, "token": token}))
        )
        message = render_to_string(
            "users/activation_email.html", {"activation_url": url}
        )

        send_mail(
            "Budget Supervisor Email Confirmation",
            message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return response


class UserActivateView(RedirectView):
    pattern_name = "login"

    def get_redirect_url(self, user_id: str, token: str) -> HttpResponseRedirect:
        user_id = force_str(urlsafe_base64_decode(user_id))
        user = User.objects.filter(pk=user_id).first()
        if user and user_tokenizer.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(self.request, "Registration complete. Please login.")
        else:
            messages.error(
                self.request,
                "Registration confirmation error. Please click the reset password to generate a new confirmation email.",
            )
        return super().get_redirect_url()


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("login")
    success_message = "User was deleted successfully"

    def get_object(self, queryset: QuerySet = None) -> Profile:
        return self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        user = self.get_object()
        if user.profile.external_id:
            remove_customer_from_saltedge(user.profile, customers_api())
        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    fields: List[str] = []
    success_url = reverse_lazy("profile")
    template_name = "users/profile_form.html"
    success_message = "Profile was updated successfully"

    def get_object(self, queryset: QuerySet = None) -> Profile:
        return self.request.user.profile


class ProfileConnectView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "users/profile_connect.html"
    form_class = ProfileConnectForm
    success_url = reverse_lazy("profile")
    success_message = "Profile was connected successfully"

    def form_valid(self, form: ProfileConnectForm) -> HttpResponseRedirect:
        profile = self.request.user.profile
        create_customer_in_saltedge(profile, customers_api())
        return super().form_valid(form)


class ProfileDisconnectView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "users/profile_disconnect.html"
    form_class = ProfileDisconnectForm
    success_url = reverse_lazy("profile")
    success_message = "Profile was disconnected successfully"

    def form_valid(self, form: ProfileDisconnectForm) -> HttpResponseRedirect:
        profile = self.request.user.profile
        remove_customer_from_saltedge(profile, customers_api())

        connections = Connection.objects.filter(user=profile.user)
        accounts = Account.objects.filter(connection__in=connections)
        accounts.update(external_id=None)
        transactions = Transaction.objects.filter(account__in=accounts)
        transactions.update(external_id=None)
        connections.delete()

        return super().form_valid(form)
