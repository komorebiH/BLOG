#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('hxl/', views.index),
    path('article_page/<int:article_id>/', views.article_page, name='article_page'),
    path('edit/<int:article_id>/', views.edit_page, name='edit_page'),
    path('edit/action/', views.edit_action, name='edit_action'),
]