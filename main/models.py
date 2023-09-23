from django.db import models


class Documentation(models.Model):

	title 		= models.CharField('Тақырыбы', max_length = 500)
	body  		= models.TextField('Түсіндірме')
	video_link	= models.TextField('Видео (Youtube)')

	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name = 'Нұсқаулық'
		verbose_name_plural = 'Нұсқаулықтар'