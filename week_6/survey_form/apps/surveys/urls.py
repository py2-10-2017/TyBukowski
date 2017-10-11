from django.conf.urls import url
from . import views

urlpatterns = [

# / 
    url(r'^$', views.survey, name='survey'),
# /result
    url(r'^result$', views.result, name='result'),
# /surveys/process
    url(r'^surveys/process$', views.process, name='process'),
]