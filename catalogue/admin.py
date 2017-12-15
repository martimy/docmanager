from django.contrib import admin

from .models import Book

# add this class to customize the display
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'seen']

admin.site.register(Book, BookAdmin)
