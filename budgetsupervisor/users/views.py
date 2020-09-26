from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileConnectForm, SignUpForm
from saltedge_wrapper.factory import customers_api


class SignUpView(CreateView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = []
    success_url = reverse_lazy("profile")
    template_name = "users/profile_form.html"

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileConnectView(LoginRequiredMixin, FormView):
    template_name = "users/profile_connect.html"
    form_class = ProfileConnectForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        profile = self.request.user.profile
        Profile.objects.create_in_saltedge(profile, customers_api())
        return super().form_valid(form)
