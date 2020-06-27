from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('transactions/', include('transactions.urls')),
    path('admin/', admin.site.urls),
]
