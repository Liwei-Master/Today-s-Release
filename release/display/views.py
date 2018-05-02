from django.shortcuts import render, redirect
from .models import Item
from user_system.models import User, History
from display.models import Item
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

    return render(request, 'display/homepage.html', context)


def recommendation():
    pass


    # 分类模块
def category(request, category):
    news = Item.objects.order_by("collect_time")
    daily_news = news.order_by('collect_time').filter(category=category)[:6]

    context = {
        'daily_news': daily_news,
        }

    return render(request, 'display/category.html', context)


def search(request):
    if request.POST:
        keywords = request.POST.get('keywords')
        result = Item.objects.filter(item_title__contains=keywords)[:6]
        context = {
            'daily_news': result,
        }

        return render(request, 'display/category.html', context)


def personal_info(request):
    user_id = request.session['user_id']
    user = User.objects.get(pk=user_id)
    history = user.history_set.all()[:10]
    labels = request.session['labels']
    if type(labels) == str:
        labels_list = labels.split("/")
        request.session['labels'] = labels_list
    return render(request, 'user_system/personal_info.html', {'history': history})


def personal_interest(request):
    return render(request, 'user_system/personal_interest.html')


def personal_warehouse(request):
    return render(request, 'user_system/personal_warehouse.html')


def click(request, url):
    item = Item.objects.get(title_link=url)
    item.view_count += 1
    item.save()
    if request.session.get('is_login', None):
        user_id = request.session['user_id']
        user = User.objects.get(pk=user_id)
        record = History(user=user, title_link=url, item_title=item.item_title)
        record.save()
    return redirect(url)