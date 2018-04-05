from django.conf.urls import url
from . import views

app_name = "experiment"

urlpatterns = [
    
    # Experiment URLS
    url(r'^researcher/experiment_list/$', views.ExperimentListView.as_view(), name='exp_list'),
    url(r'^researcher/experiment_create/$', views.ExperimentCreateView.as_view(), name='exp_create'),
    url(r'^researcher/experiment_list/(?P<pk>\d+)/$', views.ExperimentDetailView.as_view(), name='exp_detail'),
    url(r'^researcher/experiment_list/update/(?P<pk>\d+)/$', views.ExperimentUpdateView.as_view(), name='exp_update'),
    url(r'^researcher/experiment_list/delete/(?P<pk>\d+)/$', views.ExperimentDeleteView.as_view(), name='exp_delete'),
    url(r'^experiment_list_public/$', views.ExperimentPublicListView.as_view(), name='exp_list_public'),
    url(r'^experiment_list_public/(?P<pk>\d+)/$', views.ExperimentPublicTest.as_view(), name='exp_test'),

    url(r'^researcher/experiment_list/(?P<epk>\d+)/file_list/$', views.FileListView.as_view(), name='file_list'),
    #url(r'^researcher/experiment_list/file_create/$', views.FileCreateView.as_view(), name='file_create'),
    url(r'^researcher/experiment_list/(?P<epk>\d+)/file_list/delete/(?P<pk>\d+)/$', views.FileDeleteView.as_view(), name='file_delete'),

    ]



