import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_lesson.settings")
django.setup()

from orm_test.models import Author, Post

Author.objects.create(first_name = "Mykola", last_name = "Bilosvit", email = "nemo.bma@gmail.com")


author = Author.objects.filter(first_name = "Mykola").first()
author.first_name = "Anton"
author.save()
print(author)
post = Post.objects.create(title = "Post 1", body = "weqeweqweqwe", author = author)
print(post)
post = Post.objects.get(id = 1)
print(post.created_at)