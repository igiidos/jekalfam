from django.urls import path
from . import views

urlpatterns = [
	path('', views.monthly_list, name='monthly_list'),
]