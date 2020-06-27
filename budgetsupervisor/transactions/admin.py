from django.contrib import admin

from .models import Payee, Category, Transaction

admin.site.register((Payee, Category, Transaction))
