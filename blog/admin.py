from django.contrib import admin
from blog.models import Category, Post, Comment, Trend

admin.site.register([Category, Post, Comment, Trend])

