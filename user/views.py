from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from user.forms import SignUpForm, CustomLoginForm
from user.models import User, Follow
from blog.models import Post
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView, LogoutView

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:sign_in")
    else:
         form = SignUpForm()
    data = {
        "form": form,
    }
    return render(request, 'registration/signup.html', data)

class LoginView(LoginView):
    template_name = "registration/signin.html"
    authentication_form = CustomLoginForm


def dashboard(request, id):
    user = get_object_or_404(User, id=id)
    user_posts = Post.objects.filter(author=user)
    paginitor = Paginator(user_posts, 2)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginitor.page(page_number)
    except:
        posts = paginitor.page(1)

    data = {
        'user': user,
        'user_posts': user_posts,
        'posts': posts,
    }

    return render(request, 'dashboard.html', data)



def profile(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        avatar = request.FILE.get('avatar')
        phone = request.POST.get('phone')
        job = request.POST.get('job')
        bio = request.POST.get('bio')
        
        user.full_name = full_name
        user.phone = phone
        user.job = job
        user.bio = bio
        user.avatar = avatar
        user.save()
        return redirect('user:profile', user.id)

    
    try:
        status = Follow.objects.filter(user=user, follower=request.user).exists()
    except:
        status = None 

    data = {
        'user': user,
        'status': status,
    }

    return render(request, 'profile.html', data)



def follow(request, id):
    user = get_object_or_404(User, id=id)

    following, created = Follow.objects.get_or_create(
        user=user, follower=request.user
    )
    if not created:
        following.delete()

    

    return redirect('user:profile', id=user.id)



def follow_info(request, id):
    user = get_object_or_404(User, id=id)

    

    
    data = {
        'user': user,
    }

    return render(request, 'follow_info.html', data)

