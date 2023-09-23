from django.urls import path 
from . import views


urlpatterns = [
	path('', views.main_view, name = 'main'),
	path('documentation/', views.project_doc, name = 'documentation'),
]