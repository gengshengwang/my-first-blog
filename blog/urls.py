# urls
#
# Description: Enter file description here
#
# Author: watson
# Created: 2024/10/7
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name='post_list'),
]