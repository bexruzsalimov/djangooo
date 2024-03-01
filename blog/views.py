from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category
from blog.forms import CreatePostForm

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

    return render(request, 'posts/post_detail.html', data)


def post_create(request):

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']
            category_id = form.cleaned_data['category']
            category = Category.objects.get(pk=category_id)

            post = Post.objects.create(
                author=user,
                text=text,
                img=image,
                category=category,
            )
            return redirect('user:dashboard', id=user.id)
    else:
        form = CreatePostForm()

    data = {
        'form' :form,
    }

    return render(request, 'posts/post-create.html', data)

