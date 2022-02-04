from django.contrib import admin
from django.urls import re_path
from app import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^trainer$', views.trainer, name='trainer'),
    re_path(r'^team$', views.team, name='team'),
    re_path(r'^current$', views.current, name='current'),
    re_path(r'^task$', views.task, name='task'),
    re_path(r'^ass$', views.ass, name='ass'),
    re_path(r'^Trainees$', views.Trainees, name='Trainees'),
    re_path(r'^Empdetails$', views.Empdetails, name='Empdetails'),
    re_path(r'^Attendance$', views.Attendance, name='Attendance'),
    re_path(r'^task1$', views.task1, name='task1'),
    re_path(r'^List$', views.List, name='List'),
    re_path(r'^tdetails$', views.tdetails, name='tdetails'),




]
