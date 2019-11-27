from django.conf.urls import url

from . import views

urlpatterns = [
    url('^comment/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$', views.post_comment,
        name='post_comment'),
    url('^comment/(?P<comment_id>\d+)/delete/$', views.delete_comment,
        name='delete_comment'),
    url('^comment/(?P<comment_id>\d+)/edit/$', views.edit_comment,
        name='edit_comment')
]
