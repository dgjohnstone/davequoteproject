from django.conf.urls import url
from . import views     

def test(request):
    print "this is working too"

urlpatterns = [
    url(r'^dashboard$', views.dashboard), 
    url(r'^add$', views.add),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^favorite/(?P<id>\d+)$', views.favorite),
 
  ]