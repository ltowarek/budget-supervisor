from django.urls import include, path

from . import views

accounts_patterns = (
    [
        path("", views.AccountListView.as_view(), name="account_list"),
        path("create/", views.AccountCreate.as_view(), name="account_create"),
        path("<int:pk>/update", views.AccountUpdate.as_view(), name="account_update"),
        path("<int:pk>/delete", views.AccountDelete.as_view(), name="account_delete"),
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

connections_patterns = (
    [
        path("", views.ConnectionsListView.as_view(), name="connection_list"),
        path("create/", views.ConnectionCreate.as_view(), name="connection_create"),
        path(
            "<int:pk>/update",
            views.ConnectionUpdate.as_view(),
            name="connection_update",
        ),
        path(
            "<int:pk>/delete",
            views.ConnectionDelete.as_view(),
            name="connection_delete",
        ),
        path(
            "<int:pk>/refresh",
            views.ConnectionRefresh.as_view(),
            name="connection_refresh",
        ),
    ],
    "connections",
)

reports_patterns = (
    [path("income/", views.ReportIncomeView.as_view(), name="report_income")],
    "reports",
)

callbacks_patterns = (
    [
        path("success/", views.CallbackSuccess.as_view(), name="callback_success"),
        path("fail/", views.CallbackFail.as_view(), name="callback_fail"),
        path("destroy/", views.CallbackDestroy.as_view(), name="callback_destroy"),
        path("notify/", views.CallbackNotify.as_view(), name="callback_notify"),
        path("service/", views.CallbackService.as_view(), name="callback_service"),
    ],
    "callbacks",
)

urlpatterns = [
    path("", views.IndexView.as_view(), name="budget_index"),
    path("accounts/", include(accounts_patterns)),
    path("transactions/", include(transactions_patterns)),
    path("categories/", include(categories_patterns)),
    path("connections/", include(connections_patterns)),
    path("reports/", include(reports_patterns)),
    path("callbacks/", include(callbacks_patterns)),
]
