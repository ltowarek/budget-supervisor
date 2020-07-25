from django.contrib import admin

from .models import Account, Category, Connection, Transaction

admin.site.register((Account, Category, Connection, Transaction))
