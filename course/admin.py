from django.contrib import admin
from .models import *


admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(TaskIsTest)
admin.site.register(TaskIsFill)
admin.site.register(TaskIsIdentify)
admin.site.register(UserResult)
admin.site.register(SubjectLection)