from django.shortcuts import render
from .models import Documentation
# Create your views here.

def main_view(request):
	return render(request, 'main/index.html')


def project_doc(request):
	model = Documentation.objects.all()
	data = {
		'documentation': model,
	}
	return render(request, 'main/documentation.html', data)