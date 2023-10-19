from django.db import models
from course.models import Course
from django.contrib.auth.models import User


# Create your models here.
class Journal(models.Model):
	subject 	= models.ForeignKey(Course, verbose_name = 'Сабақ', on_delete = models.CASCADE)
	students	= models.ManyToManyField(User, blank = True)
	date 		= models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return str(self.subject)

	class Meta:
		verbose_name = 'Журнал'
		verbose_name_plural = 'Журналдар'