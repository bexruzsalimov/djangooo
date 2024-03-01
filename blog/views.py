from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category
from blog.forms import CreatePostForm, UpdatePostForm

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
            name = form.cleaned_data['name']
            summary = form.cleaned_data['summary']
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']
            post = Post.objects.create(
                name=name,
                summary=summary,
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


def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = UpdatePostForm(request.POST, request.FILES, instance=post)
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)           
            post.author = user
            post.save() 
            return redirect('user:dashboard', id=user.id)

    else:
        form = UpdatePostForm(instance=post)

    data = {'form': form}

    return render(request, 'posts/post-create.html', data)



def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('user:dashboard', id=request.user.id)









