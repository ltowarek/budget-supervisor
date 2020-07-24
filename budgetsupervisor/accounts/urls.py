from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.AccountListView.as_view(), name="account_list"),
    path("create/", views.AccountCreate.as_view(), name="account_create"),
    path("<int:pk>/update", views.AccountUpdate.as_view(), name="account_update"),
    path("<int:pk>/delete", views.AccountDelete.as_view(), name="account_delete"),
    path("import", views.ImportAccountsView.as_view(), name="account_import"),
    path("transactions/", views.TransactionListView.as_view(), name="transaction_list"),
    path(
        "transactions/create/",
        views.TransactionCreate.as_view(),
        name="transaction_create",
    ),
    path(
        "transactions/<int:pk>/update",
        views.TransactionUpdate.as_view(),
        name="transaction_update",
    ),
    path(
        "transactions/<int:pk>/delete",
        views.TransactionDelete.as_view(),
        name="transaction_delete",
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
    path(
        "transactions/import",
        views.ImportTransactionsView.as_view(),
        name="transaction_import",
    ),
]
