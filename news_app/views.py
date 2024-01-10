from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Detail_news

def news_view (request):
    news_list = News.objects.all()
    context = {'news_list_ht': news_list}
    # return render(request, 'html/index.html', context)
    # return render(request, 'main.html', context)
    return render(request, 'main.html', context)


def main_page(request):
    detail_news = Detail_news.objects.all()
    context = {'news_detail_page_ht': detail_news}
    return render(request, 'detail_part.html', context)