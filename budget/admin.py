from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'month', 'description', 'category', 'income', 'debits', 'balance')
    list_filter = ('month', 'category')
    search_fields = ('description', 'category')
    ordering = ('-date',)
