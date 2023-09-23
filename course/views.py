from importlib import import_module
from django.shortcuts import render, redirect
from pprint import pformat 
from .forms import TaskFillAddForm, CourseAddForm, AddCoruseForm, UserResultForm
from .models import Course, Subject, UserResult, SubjectLection
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from random import randint
from datetime import datetime
from django.http import HttpResponseRedirect
# course = ''


def course_details_view(request, pk):

	global course
	result = 'Қазірше бос'
	task_key = None
	if request.method == 'POST':
		python_cod = request.POST.get('python_cod')
		answer = 	 request.POST.get('true_answer')
		task_key = 	 request.POST.get('task_id')
		res = str(compile_user_code(python_cod, request.user)) 
		if str(res) == str(answer):
			result = 'Дұрыс'
		else:
			result = 'Қате'
	request.course = Course.objects.get(id = pk)
	# print(request.course.id)
	user_result =  UserResult.objects.filter(course = request.course, user = request.user.id)
	# print(user_result)
	data = {
		'range': [str(i) for i in range(1, 12)],
		'object_course':	request.course,
		'compiler_result':	result,
		'task_key':			task_key,
		'user_result':		user_result,
		'subject_lection': 	SubjectLection.objects.get(lesson = request.course)
	}
	return render(request, 'course/course_details.html', data)


def cod(python_cod): 
	res = list()  
	commands = python_cod.split('\n')

	for command in commands:  
		try:  
			if command.count('\r') == 1:
				command = command.replace("\r", "")
			if command[0:5] == 'print':
				command_res = eval(command[6:len(command)-1]) 
				res.append(command_res)
			elif command[0:5] == 'input':
				res.clear()
				command_res = 'input() операторын қолданба'	
				res.append(command_res)
				return res
			else:
				command_res = eval(command)
				res.append(command_res)
		except SyntaxError:
			command_res = exec(command)
			res.append(exec(command))
		except IndentationError:
			res.append('Тармақталған алгоритм қолданып керек емес!') 
	return res


def compile_user_code(python_cod, request_user):

	random_file = ''
	if not request_user.is_authenticated:
		random_file = str(randint(0, 10)) 

	commands = python_cod.split('\n')
	file_name = str(request_user) + random_file

	with open(f'course/scripts_py/{file_name}.py', mode = 'w', encoding = 'utf-8') as file:
		file.write('def run_user_script():\n')
		file.write('	result = "Нәтиже result деген айнымалыға сақталу керек"\n')

		for script in commands:
			if 'input' in script:
				return 'input() операторын қолданба!'
			else:
				file.write('	' + str(script) + '\n')
		file.write('	return result')

	script = import_module(f'course.scripts_py.{file_name}')

	try:
		return script.run_user_script()
	except SyntaxError:
		return 'Invalid syntax'

def compiler(request):
	python_cod = ''
	res = 'Нәтиже осы жерде'
	if request.method == 'POST':
		python_cod = request.POST.get('python_cod')
		res = str(compile_user_code(python_cod, request.user)) 
		redirect('compiler')

	data = {
		'compile_res': res,
		'python_cod' : python_cod,
	}

	return render(request, 'course/compiler.html', data)

def add_course(request):
	if request.method == 'POST':
		form = AddCoruseForm(request.POST) 
		message = ''
		if form.is_valid():
			form.save(commit = False) 
			form.save()
			print(form)
			return redirect('main')
			
	form = AddCoruseForm()
	data = {
		'task_add_form':form,
	}
	return render(request, 'course/create_course.html', data)



def task_add(request):
	if request.method == 'POST':
		form = TaskFillAddForm(request.POST) 
		message = ''
		if form.is_valid():
			form.save(commit = False) 
			
			form.save()
			return redirect('main')
			
	form = TaskFillAddForm()
	data = {
		'task_form':form,
	}
	return render(request, 'course/task_add.html', data)

def create_course(request):
	if request.method == 'POST':
		array = ['1', '2']
		course_id = 1
		course_obj = Course.objects.get(id = course_id)
		for i in array:
			course_obj.task_f.add(int(i))

def save_user_result(request):
	if request.method == 'POST':
		form = UserResultForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			form.date = datetime.now()
			form.user = request.user
			print(form.course.id)

			form.save()
			return HttpResponseRedirect('/course/detail/' + str(form.course.id))

	form = UserResultForm()

	data = {
		'form_result':form,
	}

	return render(request, 'course/result_save.html', data)


# class CourseDetailView(DetailView):
	# model = Course
	# template_name = 'course/course_details.html'
	# def get_context_data(self, **kwargs):
	# 	context = super(UserList, self).get_context_data(**kwargs)
	# 	context['range'] = range(1, 11)
	# 	return context


class SubjectListView(ListView):
	model = Subject
	template_name = 'course/course_main.html'

	def get_context_data(self, **kwargs):
		context = super(SubjectListView, self).get_context_data(**kwargs)
		context['range'] = [str(i) for i in range(1, 12)]
		return context


class CourseDetailResultView(DetailView):
	model = Course
	template_name = 'course/course_result.html'
	def get_context_data(self, **kwargs):
		context = super(CourseDetailResultView, self).get_context_data(**kwargs)
		context['user_results'] = UserResult.objects.filter(course = self.object.id)
		return context