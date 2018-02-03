from django.conf.urls import url
from . import views



app_name='groups'


urlpatterns=[
    url(r'^$',views.listgroup.as_view(),name='all'),
    url(r'^new/$',views.creategroup.as_view(),name='create'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$',views.singlegroup.as_view(),name='single'),
    url(r'^join/(?P<slug>[-\w]+)/$',views.joinfroup.as_view(),name='join'),
    url(r'^leave/(?P<slug>[-\w]+)/$',views.leavegroup.as_view(),name='leave'),
]