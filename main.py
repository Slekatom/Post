import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_lesson.settings")
django.setup()

from orm_test.models import Author, Post

#Author.objects.create(first_name = "Hosha", last_name = "Khrokovisch", email = "go.khro@gmail.com")


author = Author.objects.filter(first_name = "Petro").first()
# author.first_name = "Anton"
# author.save()
# print(author)
#post = Post.objects.create(title = "Roshen", body = "Coruption schema!", author = author)
# print(post)
# post = Post.objects.get(id = 1)
# print(post.created_at)