from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
]

def handler404(request):
	response = render_to_response('404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response