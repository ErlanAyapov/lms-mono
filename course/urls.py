from django.urls import path 
from . import views


urlpatterns = [
	path('', views.SubjectListView.as_view(), name = 'subject'),
	path('detail/<int:pk>', views.course_details_view, name='course_page'),
	path('result/<int:pk>', views.CourseDetailResultView.as_view(), name='user_result'),
	path('compiler/', views.compiler, name = 'compiler'),
	path('task/add/', views.task_add, name = 'task_add'),
	path('task/create/', views.add_course, name = 'add_course'),
	path('result/', views.save_user_result, name = 'save_result'),
	# path('task/compiler')
]