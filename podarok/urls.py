from django.contrib import admin
from django.urls import path, re_path
from .views import (
	posts_list,
	posts_create, 
	posts_detail,
	)

urlpatterns = [
    path('', posts_list, name='list'),
    path('create/', posts_create),
    re_path(r'^(?P<slug>[\w-]+)/$', posts_detail, name='posts_detail'),
    # re_path(r'^(?P<slug>[\w-]+)/edit/$', posts_update, name='update'),
    # re_path(r'^(?P<slug>[\w-]+)/delete/$', posts_delete),
]