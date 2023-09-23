from .forms import UserCreateForm, UserCustomerForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout 
from django.http import HttpResponseRedirect


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
			return redirect('main')
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
			return redirect('main')	 
	form = UserCustomerForm()
	data = {
		'customer_form':form,
		'day':range(1, 32, 1),
		'mounth':['Қаңтар', 'Ақпан', 'Наурыз', 'Сәуір', 'Мамыр', 'Маусым', 'Шілде', 'Тамыз', 'Қырқүйек', 'Қазан', 'Қараша', 'Желтоқсан'],
		'year':range(2013, 1970, -1),
	}
	return render(request, 'members/customer.html', data)