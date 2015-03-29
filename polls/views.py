from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext

from polls.models import Choice, Question

# The render() function takes the request object as its first argument, 
# a template name as its second argument and a dictionary as its optional third argument. 
# It returns an HttpResponse object of the given template rendered with the given context.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
		p = get_object_or_404(Question, pk=question_id)
		try:
				# request.POST is a dictionary-like object that lets you access submitted
				# data by key name. Here, request.POST['choice'] returns the ID of the 
				# selected choice as a string -- request.POST variables are always strings
				selected_choice = p.choice_set.get(pk=request.POST['choice'])

				# Will raise a key error if choice was not provided in POST data and
				# redisplay the question voting form with an error message 
		except (KeyError, Choice.DoesNotExist):
				return render(request, 'polls/detail.html', {
						'question': p,
						'error_message': "You didn't select a choice!",
					})
		else:
				selected_choice.votes += 1
				selected_choice.save()
				# Always return an HttpResponseRedirect after successfully dealing
		    # with POST data. This prevents data from being posted twice if a
		    # user hits the Back button.

				# HttpResponseRedirect takes a single argument: 
				# the URL to which the user will be redirected
				return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# ALTERNATIVES

# How to do it if you don't import Render:
# from django.template import RequestContext, loader

# What to do below if you don't import the Render function:
# Load the template polls/index.html and passes it a context
# (The context is a dictionary mapping template variable names to Python objects) See below
		
# def index(request):

# 		latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 		template = loader.get_template('polls/index.html')
# 		context = RequestContext(request, {
# 		    'latest_question_list': latest_question_list,
# 		})
# 		return HttpResponse(template.render(context))

#  --------------

# Catch with a 404 if does not exist. This works too-- 

# def detail(request, question_id):
# try: 
# 		question = Question.objects.get(pk=question_id)
# except Question.DoesNotExist:
# 		raise Http404("Question does not exist, sorry!")
# return render(request, 'polls/detail.html', {'question': question})