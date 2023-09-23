from django.urls import path 
from . import views


urlpatterns = [
	path('', views.authentication, name = 'members'),
	path('logout/', views.logout, name = 'logout'),
	path('register/', views.register, name = 'register'),
	path('customer/', views.user_customer, name = 'customer')
]