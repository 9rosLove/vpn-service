from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from user.forms import UserCreateForm, UserUpdateForm


class UserCreateView(generic.CreateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = "user/register.html"
    success_url = reverse_lazy("vpn:site-list")


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = "user/user_detail.html"

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    success_url = reverse_lazy("user:me")
    template_name = "user/user_form.html"

    def get_object(self, queryset=None):
        return self.request.user
