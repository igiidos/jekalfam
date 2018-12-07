from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.


class Loginviews(LoginView):
    template_name = 'accounts/login.html'


loginview = Loginviews.as_view()
