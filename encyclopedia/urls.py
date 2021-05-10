from django.urls import path

from . import views

import re

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/",views.index,name="wiki"),
    path("wiki/<slug:slug>/",views.entry_view,name="entry_view"),
    path("search/",views.search,name="search"),
    path("random/",views.random_page,name="random"),
    path("create/",views.create_entry,name="create"),
    path("edit/",views.edit_entry,name="edit"),
] 
