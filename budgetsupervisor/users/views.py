from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileConnectForm


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
        if not profile.external_id:
            form.create_customer(profile)
        return super().form_valid(form)
