from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Question

# The render() function takes the request object as its first argument, 
# a template name as its second argument and a dictionary as its optional third argument. 
# It returns an HttpResponse object of the given template rendered with the given context.

# Using two generic views, ListView and DetailView
# Each needs to know which model it will be acting on with the model attribute

# The DetailView generic view expects the primary key value captured from the URL 
# to be called "pk"

# By default, List view uses the template  <app name>/<model name>_list.html 
# aka: (polls/index.html)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
   		"""Return the last five published questions."""
   		return Question.objects.order_by('-pub_date')[:5]


# By default, uses the template <app name>/<model name>_detail.html 
# aka: polls/question_detail.html

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
		p = get_object_or_404(Question, pk=question_id)
		try:
			selected_choice = p.choice_set.get(pk=request.POST['choice'])
		except (KeyError, Choice.DoesNotExist):
			return render(request, 'polls/detail.html', {
				'question': p,
				'error_message': "You didn't select a choice.",
			})
		else:
			selected_choice.votes += 1
			selected_choice.save()
			return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))