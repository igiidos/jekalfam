from django.urls import path
from . import views

urlpatterns = [
	path('', views.monthly_list, name='monthly_list'),
	path('add_month/', views.add_month, name='add_month'),
	path('month_detail/<pk>/', views.month_detail, name='month_detail'),
	path('add_fee_formset/<pk>/', views.add_fee_formset, name='add_fee_formset'),
	path('month_detail/<month_pk>/fee/<detail_pk>/', views.fee_delete, name='fee_delete'),
	path('month_detail/<month_pk>/fee/<detail_pk>/update/', views.fee_update, name='fee_update'),
]
