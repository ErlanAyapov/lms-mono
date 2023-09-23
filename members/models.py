from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

	user 		 = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_day 	 = models.IntegerField('Туылған күні')
	birth_mounth = models.CharField('Туылған айы', max_length = 10)
	birth_year	 = models.IntegerField('Туылған жылы')
	students = models.ManyToManyField(User, verbose_name='Мұғалім оқушылары', blank=True, related_name = 'teacher_students')

	USER_TYPE_SELF = 'Оқушы'
	USER_TYPE_TEACHER = 'Мұғалім'

	USER_TYPE_OPTIONS = (
		(USER_TYPE_SELF, 'Оқушы'),
		(USER_TYPE_TEACHER, 'Мұғалім')
	)

	user_class = models.CharField(max_length=100,
		verbose_name='Қолданушы беделі',
		choices=USER_TYPE_OPTIONS,
		default=USER_TYPE_SELF)

	def __str__(self):
		return f'{str(self.user.first_name)} {str(self.user.last_name)}'

	class Meta:
		verbose_name = 'Қолданушы жайныда'
		verbose_name_plural = 'Қолданушылар жайныда'