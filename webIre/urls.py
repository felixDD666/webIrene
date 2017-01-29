from django.conf.urls import url

from . import views

app_name = 'webJP'
urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]