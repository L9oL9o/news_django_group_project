from django.urls import path

from news_app.views import *

# urlpatterns = [
#     path("", main_news_page, name="main-page-news"),
#     path("main/page/news", main_news_page, name="main-page-news"),
#
#     path("news/view/", detail_news_page, name="news_detail_page_ht"),
#     path("real/news/", from_real_news_view)
#
# ]


urlpatterns = [
    path("", main_news_page_view, name="main-page-news-ht"),
    path("main-news-page", main_news_page_view, name="main-page-news-ht"),

    # path('view/<path:news_path>/', main_news_page_view, name='main-page-news'),
    path("detail-news-page", detail_news_page, name="detail-news-page-ht"),
    path("real-news", from_real_news_view, name="real-news-page-ht")

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
