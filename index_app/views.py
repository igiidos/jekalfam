from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.


# def index(request):
# 	return render(request, 'index_app/index.html')


class Loginviews(LoginView):
	template_name = 'index_app/index.html'


index = Loginviews.as_view()


class LogoutViews(LogoutView):
	next_page = 'index'


logoutview = LogoutViews.as_view()
