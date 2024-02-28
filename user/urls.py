from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('regrtration/sign-up/', views.sign_up, name="sign_up"),
    path('regrtration/sign-in/', views.LoginView.as_view(), name="sign_in"),
    path('dashboard/<uuid:id>/', views.dashboard, name="dashboard"),
]