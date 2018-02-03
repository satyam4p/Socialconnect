from django.conf.urls import url
from . import views

app_name='posts'


urlpatterns=[
    url(r'^$',views.postlist.as_view(),name='all'),
    url(r'^new/$',views.createpost.as_view(),name='create'),
    url(r'by/(?P<username>[-\w]+)',views.userpost.as_view(),name='for_user'),
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.postdetail.as_view(),name='single'),
    url(r'^delete/(?P<pk>\d+)/$',views.deletepost.as_view(),name='delete'),




]
