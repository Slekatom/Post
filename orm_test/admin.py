from django.contrib import admin
from .models import Author, Post
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")


