from django.urls import path 
from . import views


urlpatterns = [
	path('', views.authentication, name = 'members'),
	path('logout/', views.logout, name = 'logout'),
	path('register/', views.register, name = 'register'),
	path('customer/', views.user_customer, name = 'customer'),
	path('profile/<int:pk>/', views.UserProfileView.as_view(), name = 'profile'),
	path('profile-update/<int:pk>/', views.UserProfileUpdateView.as_view(), name = 'update_user'),
	path('customer-update/<int:pk>/', views.CustomerUpdateView.as_view(), name = 'customer_update')
]