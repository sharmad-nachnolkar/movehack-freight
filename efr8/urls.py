from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^liner/$', views.liner,name='liner'),
    url(r'^liner-create-manifest/$', views.liner_create_manifest,name='liner_create_manifest'),
    url(r'^liner-view-manifests/$', views.liner_view_manifests,name='liner_view_manifests'),
    url(r'^port/$', views.port,name='port'),
    url(r'^transporter/$', views.transporter,name='transporter'),
]
