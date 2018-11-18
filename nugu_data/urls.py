from django.conf.urls import url
from nugu_data import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^health/$', views.health, name='health'),
    url(r'^aw_calorie/$', views.calroie, name='aw_calorie'),
    url(r'^aw_bmi/$', views.aw_bmi, name="aw_bmi"),
]