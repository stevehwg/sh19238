from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^post/100(?P<post_id>[0-9]+)/$', views.post_detail, name = 'post_detail'),
    url(r'^post/new/$', views.post_new, name = 'post_new'),
    url(r'^post/(?P<post_id>[0-9]+)/edit/$', views.post_edit, name = 'post_edit'),
    url(r'^draft/$', views.draft_post, name="draft_post"),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<post_id>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
]
