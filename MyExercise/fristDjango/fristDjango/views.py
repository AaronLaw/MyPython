from django.http import HttpResponse,Http404

def home(request):
	return HttpResponse("Hello Django!")