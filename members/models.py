from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

	user 		 = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_day 	 = models.IntegerField('День рождение')
	birth_mounth = models.CharField('Месяц рождение', max_length = 10)
	birth_year	 = models.IntegerField('Год рождение')
	students = models.ManyToManyField(User, verbose_name='Ученики', blank=True, related_name = 'teacher_students')

	USER_TYPE_SELF = 'Ученик'
	USER_TYPE_TEACHER = 'Учитель'

	USER_TYPE_OPTIONS = (
		(USER_TYPE_SELF, 'Ученик'),
		(USER_TYPE_TEACHER, 'Учитель')
	)

	user_class = models.CharField(max_length=100,
		verbose_name='Статус пользователья',
		choices=USER_TYPE_OPTIONS,
		default=USER_TYPE_SELF)
	image			= models.ImageField(upload_to ='media/uploads/user/', verbose_name = 'Изоброжение', blank=True, null = True)
	biography		= models.TextField(verbose_name = 'Биография', null = True)
	address			= models.CharField(verbose_name = 'Адрес', max_length = 255, null = True)
	phone_number	= models.CharField(verbose_name = 'Телефон', max_length = 12, blank = True, null = True)

	def __str__(self):
		return f'{str(self.user.first_name)} {str(self.user.last_name)}'

	class Meta:
		verbose_name = 'Дополнительный информация'
		verbose_name_plural = 'Дополнительные информаций'