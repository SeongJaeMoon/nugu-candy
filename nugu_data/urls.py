from django.conf.urls import url
from nugu_data import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^health/$', views.health, name='health'),
    url(r'^awCalorie/$', views.awCalorie, name='awCalorie'),
    url(r'^awBmi/$', views.awBmi, name="awBmi"),
]