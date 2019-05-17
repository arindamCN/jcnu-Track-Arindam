from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'api/1', views.AddView.as_view(), name='addPerson'),
    url(r'api/2', views.AddMenteeView.as_view(), name='addMentee'),
    url(r'api/3', views.ShowMenteesView.as_view(), name='showMentees'),
]