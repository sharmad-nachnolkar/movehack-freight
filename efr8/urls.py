from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^liner/$', views.liner,name='liner'),
    url(r'^port/$', views.port,name='port'),
    url(r'^transporter/$', views.transporter,name='transporter'),
]
