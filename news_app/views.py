from django.shortcuts import render
from .models import News

def news_view (request):
    news_list = News.objects.all()
    context = {'news_list_ht': news_list}
    # return render(request, 'html/index.html', context)
    # return render(request, 'main.html', context)
    return render(request, 'main.html', context)


def main_page(request):
    context = {'news_list_ht': news_list}

    return render(request, 'news_django.html')