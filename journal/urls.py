from django.urls import path 
from . import views


urlpatterns = [ 
	path('', views.JournalCreateView.as_view(), name = 'create_journal'),
	path('add-student/<int:pk>', views.add_student, name = 'add_student'),
	path('check-student/<int:pk>', views.check_sudents, name = 'check_student'),
	# path('generate_qr_code/', views.current_page_with_qr, name='current_page_with_qr'),
	path('journal-details/<int:pk>', views.JournalDetailsView.as_view(), name = 'journal_details')
]