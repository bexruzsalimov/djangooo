from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


def home(request):
    posts = Post.objects.all()
    posts_sponsored = Post.objects.filter(status=True)

    data = {
        'posts': posts,
        'posts_sponsored':  posts_sponsored    
    }

    return render(request, 'home.html', data)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    data = {
        'post': post,
    }

    return render(request, 'post_detail.html', data)

