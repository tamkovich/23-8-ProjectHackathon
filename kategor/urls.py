from django.urls import path, re_path, include
from django.views.generic import ListView, DetailView
from . import views
from django.conf.urls import url
from kategor.models import Categories
from tovar.models import Product
from tovar import views as views_t

urlpatterns = [
	path('', views.all_cat),
	re_path(r'^(?P<slug>[\w-]+)$', views.spec_cat, name='spec_cat'),
	re_path(r'^(?P<cat_slug>[\w-]+)/(?P<slug>[\w-]+)/$', views_t.spec_prod),
]