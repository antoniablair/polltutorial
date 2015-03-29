from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'polltutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
		# url(r'^detail/', include(detail.site.urls)),
		# url(r'^results/', include(results.site.urls)),
		# url(r'^vote/', include(vote.site.urls)),
)