from django.contrib import admin
from django.urls import path

from news_app.views import *

urlpatterns = [
    path("", news_view, name="news_view_ht"),
    path("news_django_page", main_page, name="news_django_page_ht")
]
