from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
        # ex: /polls/5/
        # ?P< > mean it will use the view to determine what to do there
        # (without the ?P it would be an unnamed capture group, like just parenthesis)
        # \d means it is a digit
        # therefor ?P<question_id>\d will look for a number
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)