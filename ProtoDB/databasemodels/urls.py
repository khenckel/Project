from django.conf.urls import patterns, url
from databasemodels import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /database/
    
    url(r'^(?P<protocol_id>\d+)/$', views.procedure, name='procedure'),
    # ex: /database/5/
    
     url(r'^(?P<protocol_id>\d+)/details/$', views.details, name='details'),
    # ex: /database/5/details
    
    url(r'^(?P<protocol_id>\d+)/rating/$', views.rating, name='rating'),
     # ex: /database/5/rating/
  
    url(r'^(?P<protocol_id>\d+)/favorite/$', views.favorite, name='favorite'),
    # ex: /database/5/favorite/
)
