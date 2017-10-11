from django.conf.urls import url
from . import views

app_name = 'rwg'

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^random_word$', views.generate, name='generate'),
    url('^reset$', views.reset, name='reset'),
]