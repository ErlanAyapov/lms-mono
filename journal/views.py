import requests 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Journal
from course.models import Course, Subject
from .forms import JournalForm
from django.views.generic.edit import CreateView
from django.urls import reverse
import base64
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class JournalDetailsView(DetailView):
	model = Journal
	template_name = 'journal/journal_detail.html'

	def get_context_data(self, **kwargs): 
		context = super( JournalDetailsView, self ).get_context_data( **kwargs )
		current_url = self.request.build_absolute_uri()
		api_url = f'https://api.qrserver.com/v1/create-qr-code/?data={current_url}&size=200x200'
		response = requests.get(api_url)
		image_base64 = base64.b64encode(response.content).decode('utf-8')

		joqtar = list()
		journal = self.object 

		course = Course.objects.get(id=self.object.subject.id )
		subjects_related_to_course = course.course_sbj.all()

		for subject in subjects_related_to_course:
			subject_id = subject.id
		students_subject = Subject.objects.get(id = subject_id).students.all()
		for item in students_subject:
			if item not in self.object.students.all():
				joqtar.append(item)


		context = {
			'current_url': current_url,
			'image_base64':image_base64,
			'obj':self.object,
			'joqtar':joqtar,
		}
		return context
# Create your views here.
class JournalCreateView(CreateView):
	model = Journal
	template_name = 'journal/journal.html'
	fields = ('__all__')

	def get_success_url(self):
		print(self.object.id)
		return reverse('journal_details', args=[str(self.object.id)])


def add_student(request, pk):
	journal = Journal.objects.get(pk = pk)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		student = User.objects.filter(first_name =first_name, last_name = last_name)
		if len(student) == 1: 
			print(journal.students.add(student[0].id))
			return redirect('main')


	return render(request, 'journal/addstudent.html')


def check_sudents(request, pk):
	b = 0
	joqtar = list()
	journal = Journal.objects.get(pk = pk)
	students_journal= journal.students.all()
	students_subject = journal.subject.students.all() 
	for item in students_subject:
		if item not in students_journal:
			joqtar.append(item)

	print(joqtar, list(students_subject))
 
	return HttpResponse(joqtar, status=200)

