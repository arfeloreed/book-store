from django.contrib import admin
from .models import Book, Author, Address, Country


# manipulating the admin display
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
