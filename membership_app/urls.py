from django.urls import path
from . import views

urlpatterns = [
	path('', views.monthly_list, name='monthly_list'),
	path('add_month/', views.add_month, name='add_month'),
	path('month_detail/<pk>/', views.month_detail, name='month_detail'),
	path('add_fee_formset/<pk>/', views.add_fee_formset, name='add_fee_formset'),
]
