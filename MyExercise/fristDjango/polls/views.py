# Create your views here.
#from django.template import Context,loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from models import Poll,Choice
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse

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
	poll = get_object_or_404(Poll,pk=poll_id)
	return render(request,'polls/results.html',{'poll':poll})

def vote(request,poll_id):
	p = get_object_or_404(Poll,pk=poll_id)
	try:
		select_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'pool':p,
			'error_message':'You didn\'t select a choice.',
			})
	else:
		select_choice.votes += 1
		select_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
'''
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
'''