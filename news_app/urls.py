from django.contrib import admin
from django.urls import path

from news_app.views import *

urlpatterns = [
    path("", news_view, name="news_view_ht"),
    path("news_view_ht", news_view, name="news_view_ht" ),

    path("news_detail_page_ht", main_page, name="news_detail_page_ht")
]
