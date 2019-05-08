from django.conf.urls import url

from . import views

urlpatterns = [
	url('', views.index, name='index'),
	url('room_name/', views.room, name='room'),
]