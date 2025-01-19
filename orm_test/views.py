from django.shortcuts import render
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_lesson.settings")
django.setup()

from orm_test.models import Author, Post
# Create your views here.
def main(request):
    return render(request, "main_page.html")
def author(request):
    authors = Author.objects.all()
    return render(request, "authors_page.html", {"authors": authors})
def posts(request):
    posts = Post.objects.all()
    return render(request, "posts_page.html", {"posts": posts})