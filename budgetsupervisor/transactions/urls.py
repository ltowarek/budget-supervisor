from django.urls import path

from . import views

app_name = 'transactions'
urlpatterns = [
    path('', views.TransactionListView.as_view(), name='transaction_list'),
    path('create/', views.TransactionCreate.as_view(), name='transaction_create'),
    path('<int:pk>/update', views.TransactionUpdate.as_view(), name='transaction_update'),
    path('<int:pk>/delete', views.TransactionDelete.as_view(), name='transaction_delete'),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete', views.CategoryDelete.as_view(), name='category_delete'),
]
