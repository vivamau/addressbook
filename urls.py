from django.conf.urls import patterns, url

from addressbook import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<account_id>\d+)/$', views.account, name='account'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^search2/(?P<query>\w+)/$', views.search2, name='search2'),
    url(r'^search/', views.search, name='search'),
)