from django import forms
from .models import TaskIsFill, Course, UserResult
from django.contrib.admin.widgets import FilteredSelectMultiple


class TaskFillAddForm(forms.ModelForm):
	class Meta:
		model = TaskIsFill
		fields = ('__all__')


class CourseAddForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ('__all__')


class AddCoruseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('__all__')
        widgets = {
            'task_f': FilteredSelectMultiple(u'Тапсырма түрі (Код және бос орын)', False),
        }
    class Media:
        css = {
            'all': ['admin/css/widgets.css'],
        }
        js = ['/admin/jsi18n/']


class UserResultForm(forms.ModelForm):
    class Meta:
        model = UserResult
        fields = ('course', 'all_task', 'true_task', 'false_task', 'feedback', 'user_false_answers')
        exclude = ['user', 'date']