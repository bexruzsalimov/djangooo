from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from user.forms import SignUpForm, CustomLoginForm
from user.models import User
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
    paginitor = Paginator(user_posts, 1)
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
