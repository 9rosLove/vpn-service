from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from vpn.forms import SiteForm
from vpn.models import Site


class SiteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Site
    form_class = SiteForm
    success_url = reverse_lazy("vpn:site-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class SiteListView(LoginRequiredMixin, generic.ListView):
    model = Site
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)


class SiteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Site
    success_url = reverse_lazy("vpn:site-list")


class SiteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Site
    form_class = SiteForm
    success_url = reverse_lazy("vpn:site-list")
