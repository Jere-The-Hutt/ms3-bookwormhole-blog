from django.contrib import admin
from contact.models import Contact


# Register your models here.
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name', 'email', 'book_title', 'submitted_at')
    search_fields = ('name', 'email', 'book_title', 'book_author', 'message')
    readonly_fields = ('name', 'email', 'book_title', 'book_author', 'message', 'submitted_at')
    list_filter = ('submitted_at',)
    ordering = ('-submitted_at',)
