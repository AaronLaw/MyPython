# Create your views here.
from django.http import HttpResponse,Http404
from models import Poll
#from django.template import Context,loader
from django.shortcuts import render

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {'latest_poll_list':latest_poll_list}
	return render(request,'polls/index.html',context)

def detail(request,poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		#return render(request,'404.html')	
		raise Http404
	return render(request,'polls/detail.html',{"poll":poll})	

def results(request,poll_id):
	return HttpResponse("You're looking at the results of poll %s."%poll_id) 
def vote(request,poll_id):
	return HttpResponse("You're voting on poll %s."%poll_id)