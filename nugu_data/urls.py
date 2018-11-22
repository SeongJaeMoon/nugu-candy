from django.conf.urls import url
from nugu_data import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^health$', views.health, name='health'),
    url(r'^awCalorie$', views.awCalorie, name='awCalorie'),
    url(r'^awBmi$', views.awBmi, name="awBmi"),
    url(r'^awCalts$', views.awCalts, name="awCalts"),
    url(r'^awEnergy$', views.awEnergy, name="awEnergy"),
]