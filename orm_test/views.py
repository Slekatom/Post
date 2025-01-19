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
    #posts = Post.objects.filter(published = True)
    posts = Post.objects.all()
    return render(request, "posts_page.html", {"posts": posts})

def get_post_by_id(request, post_id):
    post = Post.objects.get(id = post_id)
    cont = {
        "post": post
    }
    return render(
        request, "post_id_page.html", cont
    )
def get_post_by_author(request, author):
    posts = Post.objects.filter(author__first_name = author)
    cont = {
        "posts": posts,
        "author": author
    }
    return render(
        request, "post_author_page.html", cont
    )
