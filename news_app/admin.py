# from django.contrib import admin
# from django.contrib.admin import ModelAdmin
#
# from .models import News, Detail_news, From_real_news
#
# admin.site.register(Detail_news)
# admin.site.register(From_real_news)
from django.contrib import admin
from django.contrib.admin import ModelAdmin
# from django.contrib.auth import admin

from .models import News, Detail_news, From_real_news


class NewsModelAdmin(ModelAdmin):
    list_display = ('title',)


class DetailNewsAdmin(ModelAdmin):
    list_display = ('title',)


class RealNewsAdmin(ModelAdmin):
    list_display = ("title",)


admin.site.register(News, NewsModelAdmin)
admin.site.register(Detail_news, DetailNewsAdmin)
admin.site.register(From_real_news, RealNewsAdmin)
