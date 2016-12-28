from django.conf.urls import url

from . import views


app_name = 'polls'

urlpatterns = [
    # /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # /polls/nueva/
    url(r'^nueva/$', views.CreateQuestionView.as_view(), name='nueva'),
    # /polls/nueva2/
    url(r'^manage/$', views.manage_questions, name='manage'),


]
