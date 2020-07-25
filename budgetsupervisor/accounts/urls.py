from django.urls import include, path

from . import views

accounts_patterns = (
    [
        path("", views.AccountListView.as_view(), name="account_list"),
        path("create/", views.AccountCreate.as_view(), name="account_create"),
        path("<int:pk>/update", views.AccountUpdate.as_view(), name="account_update"),
        path("<int:pk>/delete", views.AccountDelete.as_view(), name="account_delete"),
        path("import", views.ImportAccountsView.as_view(), name="account_import"),
    ],
    "accounts",
)

transactions_patterns = (
    [
        path("", views.TransactionListView.as_view(), name="transaction_list",),
        path("create/", views.TransactionCreate.as_view(), name="transaction_create",),
        path(
            "<int:pk>/update",
            views.TransactionUpdate.as_view(),
            name="transaction_update",
        ),
        path(
            "<int:pk>/delete",
            views.TransactionDelete.as_view(),
            name="transaction_delete",
        ),
        path(
            "import", views.ImportTransactionsView.as_view(), name="transaction_import",
        ),
    ],
    "transactions",
)

categories_patterns = (
    [
        path("", views.CategoryListView.as_view(), name="category_list"),
        path("create/", views.CategoryCreate.as_view(), name="category_create"),
        path(
            "<int:pk>/update", views.CategoryUpdate.as_view(), name="category_update",
        ),
        path(
            "<int:pk>/delete", views.CategoryDelete.as_view(), name="category_delete",
        ),
    ],
    "categories",
)

urlpatterns = [
    path("accounts/", include(accounts_patterns)),
    path("accounts/<int:account_id>/transactions/", include(transactions_patterns)),
    path("categories/", include(categories_patterns)),
]
