from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'^artigo/(?P<ano>[0-9]{4})/$', views.Artigo),
]