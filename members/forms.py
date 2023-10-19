from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput
from members.models import Customer


class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')


class UserCustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = (
			'user',
			'birth_day',
			'birth_mounth',
			'birth_year'
			) 
		# ['user', 'position']

class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')
		widgets = {
			'username':   TextInput(attrs={'class': 'form-control','placeholder': 'Қолданушы атауы',}),
			'email': 	  TextInput(attrs={'class': 'form-control','placeholder': 'почта',}),
			'first_name': TextInput(attrs={'class': 'form-control','placeholder': 'Есімі',}),
			'last_name':  TextInput(attrs={'class': 'form-control','placeholder': 'Тегі',}),
			}


class CustomerFormUpdate(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('__all__')
		exclude = ['user', 'user_class', 'students']