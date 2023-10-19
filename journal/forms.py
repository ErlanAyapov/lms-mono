from django import forms
from .models import Journal



class JournalForm(forms.ModelForm):
	class Meta:
		model = Journal
		fields = ('__all__')

class JournalAddForm(forms.ModelForm):
	class Meta:
		model = Journal
		fields = ('__all__')