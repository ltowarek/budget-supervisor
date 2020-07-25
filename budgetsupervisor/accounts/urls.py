from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.AccountListView.as_view(), name="account_list"),
    path("create/", views.AccountCreate.as_view(), name="account_create"),
    path("<int:pk>/update", views.AccountUpdate.as_view(), name="account_update"),
    path("<int:pk>/delete", views.AccountDelete.as_view(), name="account_delete"),
    path("import", views.ImportAccountsView.as_view(), name="account_import"),
    path(
        "<int:account_id>/transactions/",
        views.TransactionListView.as_view(),
        name="transaction_list",
    ),
    path(
        "<int:account_id>/transactions/create/",
        views.TransactionCreate.as_view(),
        name="transaction_create",
    ),
    path(
        "<int:account_id>/transactions/<int:pk>/update",
        views.TransactionUpdate.as_view(),
        name="transaction_update",
    ),
    path(
        "<int:account_id>/transactions/<int:pk>/delete",
        views.TransactionDelete.as_view(),
        name="transaction_delete",
    ),
    path(
        "<int:account_id>/transactions/import",
        views.ImportTransactionsView.as_view(),
        name="transaction_import",
    ),
    path("category/", views.CategoryListView.as_view(), name="category_list"),
    path("category/create/", views.CategoryCreate.as_view(), name="category_create"),
    path(
        "category/<int:pk>/update",
        views.CategoryUpdate.as_view(),
        name="category_update",
    ),
    path(
        "category/<int:pk>/delete",
        views.CategoryDelete.as_view(),
        name="category_delete",
    ),
]
