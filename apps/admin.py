from django.contrib import admin
from .models import Book, Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'address', 'active', 'slug',)
    list_editable = ('active', )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'isbn', 'price',)
    list_filter = ('published_by', 'price', )
    search_fields = ('name', 'isbn',)
