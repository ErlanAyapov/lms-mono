from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput
from members.models import Customer


class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'first_name', 'last_name')


class UserCustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = (
			'user',
			'birth_day',
			'birth_mounth',
			'birth_year'
			)