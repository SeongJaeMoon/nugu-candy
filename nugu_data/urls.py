from django.conf.urls import url
from nugu_data import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calorie/$', views.calroie, name='calroie'),
]