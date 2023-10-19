from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout 
from .models import Customer
from course.models import UserResult
from datetime import datetime
from .forms import UserCreateForm, UserUpdateForm, CustomerFormUpdate, UserCustomerForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
def logout(request):
	django_logout(request)
	return redirect('members')


def authentication(request):
	error = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None: 
			login(request, user)
			return HttpResponseRedirect('/members/profile/' + str(request.user.id))
		else:
			error = 'Қолданушы атауы мен құпия сөз сәйкес емес!'
			return render(request, 'members/auth.html', {'error':error})	
	return render(request, 'members/auth.html')


def register(request):
	error = ''
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST.get('username')  
			password = request.POST.get('password1')  
			user = authenticate(request, username = username, password = password)
			if user is not None: 
				login(request, user) 
				return redirect('customer')

		else:
			error = 'Пороли не совпадает или логин занят!'
			data = {
				'register_form':form,
				'message':error,
			}
			return render(request, 'members/register.html', data)
	else:
		form = UserCreateForm()
	return render(request, 'members/register.html', {'register_form':form})


def user_customer(request):
	if request.method == 'POST':
		form = UserCustomerForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			form.user = request.user
			form.save()
			return HttpResponseRedirect('/members/profile/' + str(request.user.id))	 
	form = UserCustomerForm()
	data = {
		'customer_form':form,
		'day':range(1, 32, 1),
		'mounth':['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
		'year':range(2013, 1970, -1),
	}
	return render(request, 'members/customer.html', data)


class UserProfileView(DetailView):
	model = User
	template_name = 'members/profile.html'

	def get_context_data(self, **kwargs): 
		context = super( UserProfileView, self ).get_context_data( **kwargs )
		context['customer'] = Customer.objects.get(user = self.request.user)
		context['results'] = UserResult.objects.filter(user = self.request.user)
		return context


class UserProfileUpdateView(UpdateView):
	model = User
	form_class = UserUpdateForm
	template_name = 'members/update.html'
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/members/profile/' + str(self.request.user.id))


class CustomerUpdateView(UpdateView):
	model = Customer
	form_class = CustomerFormUpdate
	template_name = 'members/customer_update.html'
	def form_valid(self, form):
		form = form.save(commit=False)
		form.user = self.request.user
		print(form.user)
		form.save()
		return HttpResponseRedirect('/members/profile/' + str(self.request.user.id))