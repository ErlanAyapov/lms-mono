from django.db import models
from django.contrib.auth.models import User
from members.models import Customer
from ckeditor.fields import RichTextField


COURSE_TYPE_SELF = '1' 

COURSE_TYPE_OPTIONS = (
	(COURSE_TYPE_SELF, '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
	('11', '11'),
)
SUBJECT_TYPE_SELF = 'В платформе'

SUBJECT_TYPE_OPTIONS = (
	('OP', SUBJECT_TYPE_SELF),
	('IN', 'Индивидуальный')

)

class TaskIsIdentify(models.Model):
	title	= models.CharField('Заголовок заданий ', max_length = 1000)
	body 	= models.TextField('Текст заданий')

	task_1		= models.CharField('Вопрос', max_length = 200)
	task_2		= models.CharField('Вопрос', max_length = 200)
	task_3		= models.CharField('Вопрос', max_length = 200)
	task_4		= models.CharField('Вопрос', max_length = 200)

	answer_1	= models.CharField('Ответ', max_length = 200)
	answer_2	= models.CharField('Ответ', max_length = 200)
	answer_3	= models.CharField('Ответ', max_length = 200)
	answer_4	= models.CharField('Ответ', max_length = 200)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Задание'
		verbose_name_plural = 'Задание (Сопоставить)'


class TaskIsFill(models.Model):
	title	= models.CharField('Заголовок задание', max_length = 1000)
	body 	= models.TextField('Вопрос')
	answer 	= models.CharField('Ответ', max_length = 100)

	TASK_TYPE_FILL = 'Завершит код'
	TASK_TYPE_SELF = 'Заполнит пустую линию'

	TASK_TYPE_OPTIONS = (
		(TASK_TYPE_SELF, TASK_TYPE_SELF),
		(TASK_TYPE_FILL, TASK_TYPE_FILL)
	)

	t_type	= models.CharField(max_length=100,
		verbose_name='Тип заданий',
		choices=TASK_TYPE_OPTIONS,
		default=TASK_TYPE_SELF)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Задание '
		verbose_name_plural = 'Задание (Заполнит)'


class TaskIsTest(models.Model):
	title			= models.CharField('Заголовок задание', max_length = 200)
	body			= models.TextField('Вопрос')
	answer_true		= models.CharField('Ответ', max_length = 200)
	answer_1	= models.CharField('Вариант (1)', max_length = 200)
	answer_2	= models.CharField('Вариант (2)', max_length = 200)
	answer_3	= models.CharField('Вариант (3)', max_length = 200)
	answer_4	= models.CharField('Вариант (4)', max_length = 200, default = 'Нұсқа (4)')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Задание'
		verbose_name_plural = 'Задание (Тест)'


class Course(models.Model):
	title	= models.CharField('Сабақ тақырыбы', max_length = 75)
	date	= models.DateTimeField('Сабақ уақыты')
	teacher	= models.ForeignKey(User, verbose_name = 'Сабақты қосты', on_delete = models.CASCADE)
	task_f	= models.ManyToManyField(TaskIsFill, verbose_name='Тапсырма түрі (Код және бос орын)', blank=True, related_name = 'course_task')
	task_t	= models.ManyToManyField(TaskIsTest, verbose_name='Тапсырма түрі (Тест)', blank=True, related_name = 'course_task')
	task_i 	= models.ManyToManyField(TaskIsIdentify, verbose_name='Тапсырма түрі (Сәйкестендір)', blank=True, related_name = 'course_task')
	# date_time = models.DateTimeField('Сабақ уақыты')
	course_type = models.CharField(verbose_name = 'Сабақ түрі', choices = SUBJECT_TYPE_OPTIONS, default = SUBJECT_TYPE_SELF, max_length = 50)

	synup	= models.CharField(max_length=100,
		verbose_name='Сыныпты көрсетіңіз',
		choices=COURSE_TYPE_OPTIONS,
		default=COURSE_TYPE_SELF)



	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Урок'
		verbose_name_plural = 'Уроки'

class Subject(models.Model):
	title	 = models.CharField('Пән атауы', max_length = 25)
	teachers = models.ManyToManyField(Customer, verbose_name='Пән мұғалімдері', blank=True, related_name = 'teacher_sbj')
	course	 = models.ManyToManyField(Course, verbose_name='Сабақтар', blank=True, related_name = 'course_sbj')
	students = models.ManyToManyField(User, verbose_name = 'Студенттер')
	subject_type = models.CharField(verbose_name = 'Сабақ түрі', choices = SUBJECT_TYPE_OPTIONS, default = SUBJECT_TYPE_SELF, max_length = 50)
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Предмет'
		verbose_name_plural = 'Предметы'

class SubjectLection(models.Model):
	lesson 				= models.OneToOneField(Course, verbose_name = 'Сабақ', on_delete = models.CASCADE, null = True)
	title				= models.CharField('Лекция тақырыбы', max_length = 125)
	body 	 			= RichTextField(verbose_name = 'Лекция мәтіні')
	youtube_iframe_tag 	= models.CharField('Видео ролик (Iframe)', max_length = 1000)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Лекция'
		verbose_name_plural = 'Лекций'


class UserResult(models.Model):

	user 		= models.ForeignKey(User, on_delete = models.CASCADE)
	course 		= models.ForeignKey(Course, on_delete = models.CASCADE, default = 0)
	all_task	= models.CharField('Жалпы сұрақ', max_length = 3)
	true_task	= models.CharField('Дұрыс сұрақ', max_length = 3)
	false_task	= models.CharField('Қате сұрақ', max_length = 3)
	date 		= models.CharField('Уақыты', max_length = 35, default = 'Белгісіз')
	feedback 	= models.CharField('Кері байланыс', max_length = 520, default = 'Кері байланыс жоқ')
	user_false_answers = models.TextField('Қате сұрақтар', blank = True, default = 'Қате сұрақтар белгісіз')
	
	def __str__(self):
		return f'{str(self.user.first_name)} {str(self.user.last_name)} - | - {self.feedback}'

	class Meta:
		verbose_name = 'Результат'
		verbose_name_plural = 'Результаты'