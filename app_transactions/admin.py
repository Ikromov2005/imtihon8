from django.contrib import admin

from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date', 'user')
    search_fields = ('description', 'user__username')
    list_filter = ('date', 'user')

admin.site.register(Transaction, TransactionAdmin)