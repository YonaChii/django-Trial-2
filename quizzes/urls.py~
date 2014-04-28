from django.conf.urls import patterns, url
from quizzes import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<exam_id>\d+)/$', views.examination, name='examination'),
	url(r'^(?P<exam_id>\d+)/answer/$', views.answer, name='answer'),
	url(r'^(?P<exam_id>\d+)/result/$', views.result, name='result'),
)
