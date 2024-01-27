from django.urls import path

from vpn.views import SiteListView, SiteCreateView, SiteDeleteView, SiteUpdateView

urlpatterns = [
    path("sites/", SiteListView.as_view(), name="site-list"),
    path("sites/create/", SiteCreateView.as_view(), name="site-create"),
    path("sites/<int:pk>/delete/", SiteDeleteView.as_view(), name="site-delete"),
    path("sites/<int:pk>/update/", SiteUpdateView.as_view(), name="site-update"),
]

app_name = "vpn"
