from django.shortcuts import render
from .models import Item
from user_system.models import User
# python manage.py startapp name


# Create your views here.

def index(request):
    admired_category = "搞笑"
    if request.session.get('is_login', None):
        #
        admired_category = request.session

    news = Item.objects.order_by("collect_time")
    daily_news = Item.objects.order_by("collect_time")[:6]
    daily_news_list = Item.objects.order_by("collect_time")[6:16]

    recommended_news = news.order_by('collect_time').filter(category=admired_category)[:6]
    recommended_news_list = Item.objects.order_by("collect_time").filter(category=admired_category)[6:16]

    #
    hit_news = news.order_by('collect_time')[:6]
    hit_news_list = news.order_by('collect_time')[6:16]

    context = {'daily_news': daily_news,
               'daily_news_list': daily_news_list,
               'recommended_news': recommended_news,
               'recommended_news_list': recommended_news_list,
               'hit_news': hit_news,
               'hit_news_list': hit_news_list,
               }

    return render(request, 'homepage.html', context)


def recommendation():
    pass

    # 分类模块
def categoryaction(request):

    pass

