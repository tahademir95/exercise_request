from django.conf.urls import include, url
from django.contrib import admin

from x27_app import views

urlpatterns = [
    url(r'^$', views.Index, name="index"),
    url(r'^ekle',views.ekle,name="ekle"),
    url(r'^gonder',views.gonder,name="gonder"),
    url(r'^yaz',views.yaz,name="yaz"),
    url(r'^halil',views.halil,name="halil"),

]
