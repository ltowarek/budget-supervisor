from typing import List

from budget.models import Account, Connection, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView, UpdateView
from saltedge_wrapper.factory import customers_api

from .forms import ProfileConnectForm, ProfileDisconnectForm, SignUpForm
from .models import Profile


class SignUpView(CreateView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")


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
        Profile.objects.create_in_saltedge(profile, customers_api())
        return super().form_valid(form)


class ProfileDisconnectView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "users/profile_disconnect.html"
    form_class = ProfileDisconnectForm
    success_url = reverse_lazy("profile")
    success_message = "Profile was disconnected successfully"

    def form_valid(self, form: ProfileDisconnectForm) -> HttpResponseRedirect:
        profile = self.request.user.profile
        Profile.objects.remove_from_saltedge(profile, customers_api())

        connections = Connection.objects.filter(user=profile.user)
        accounts = Account.objects.filter(connection__in=connections)
        accounts.update(external_id=None)
        transactions = Transaction.objects.filter(account__in=accounts)
        transactions.update(external_id=None)
        connections.delete()

        return super().form_valid(form)


# TODO: ProfileDeleteView
