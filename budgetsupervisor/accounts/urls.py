from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.AccountListView.as_view(), name="account_list"),
    path("create/", views.AccountCreate.as_view(), name="account_create"),
    path("<int:pk>/update", views.AccountUpdate.as_view(), name="account_update"),
    path("<int:pk>/delete", views.AccountDelete.as_view(), name="account_delete"),
    path("import", views.ImportAccountsView.as_view(), name="account_import"),
]
