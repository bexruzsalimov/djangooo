from django.contrib import admin
from blog.models import Category, Post, Comment

admin.site.register([Category, Post, Comment])

