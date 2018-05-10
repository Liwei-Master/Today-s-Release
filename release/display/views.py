from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Item
from user_system.models import User, History, Interest, Collection, Label
from display.models import Item, Images
from django.http import JsonResponse
import json
# python manage.py startapp name


# Create your views here.

def index(request, **kwargs):
    news = Item.objects.order_by("collect_time")
    daily_news = Item.objects.order_by("collect_time")[:6]
    pictures = Images.objects.order_by("collect_time")[:6]
    daily_news = zip(daily_news, pictures)
    daily_news_list = Item.objects.order_by("collect_time")[6:16]
    # 配图展示
    recommended_news = []
    # 仅标题展示
    recommended_news_list = []
    # 过滤已收藏标题
    collection_list = []

    if request.session.get('is_login', None):
        user_id = request.session['user_id']
        user = User.objects.get(pk=user_id)

        for item in user.label_set.all():
            for info in item.collection_set.all():
                collection_list.append(info.item_title)

        interest = user.interest
        if interest.first_interest:
            first_interest = interest.first_interest
            recommended_news_first = news.order_by('collect_time').filter(category=first_interest)[:5]
            recommended_news.extend(recommended_news_first)

            recommended_news_list_first = news.order_by('collect_time').filter(category=first_interest)[5:11]
            recommended_news_list.extend(recommended_news_list_first)

        if interest.second_interest:
            second_interest = interest.second_interest
            recommended_news_second = news.order_by('collect_time').filter(category=second_interest)[:3]
            recommended_news.extend(recommended_news_second)

            recommended_news_list_second = news.order_by('collect_time').filter(category=second_interest)[3:7]
            recommended_news_list.extend(recommended_news_list_second)

        if interest.third_interest:
            third_interest = interest.third_interest
            recommended_news_third = news.order_by('collect_time').filter(category=third_interest)[:2]
            recommended_news.extend(recommended_news_third)

            recommended_news_list_third = news.order_by('collect_time').filter(category=third_interest)[2:4]
            recommended_news_list.extend(recommended_news_list_third)

    #
    hit_news = news.order_by('collect_time')[:6]
    hit_news_list = news.order_by('collect_time')[6:16]

    context = {'daily_news': daily_news,
               'pictures': pictures,
               'daily_news_list': daily_news_list,
               'recommended_news': recommended_news,
               'recommended_news_list': recommended_news_list,
               'hit_news': hit_news,
               'hit_news_list': hit_news_list,
               'collection_list': collection_list,
               'info': kwargs.get('info', '初次见面，请多关注！')
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

    return render(request, 'user_system/personal_info.html', {'history': history})


def personal_interest(request, **kw):
    user_id = request.session['user_id']
    user = User.objects.get(pk=user_id)
    history = user.history_set.all()[:10]

    interest = user.interest
    if interest.first_interest:
        first = interest.first_interest
    else:
        first = '什么都没有留下'

    if interest.second_interest:
        second = interest.second_interest
    else:
        second = '什么都没有'

    if interest.third_interest:
        third = interest.third_interest
    else:
        third = '一片空白'

    if interest.key_words:
        keywords = interest.key_words
    else:
        keywords = '什么都没有留下'

    error_info = kw.get('error_info', '我们会根据你的喜好顺序给小伙伴们推荐消息，同时支持关键字推荐哦.')
    title = kw.get('title', '听我说哈')

    context = {
        'history': history,
        'first': first,
        'second': second,
        'third': third,
        'keywords': keywords,
        'error_info': error_info,
        'title': title,
    }
    return render(request, 'user_system/personal_interest.html', context)


def personal_warehouse(request):
    user_id = request.session['user_id']
    user = User.objects.get(pk=user_id)
    history = user.history_set.all()[:10]

    context = {
        'history': history
    }

    return render(request, 'user_system/personal_warehouse.html', context)


# 监听每次点击
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

def modify_interest(request):
    user_id = request.session['user_id']
    user = User.objects.get(pk=user_id)
    interest = user.interest
    if request.method == 'POST':
        title = '提示你哦：'

        first = request.POST.get('first')
        second = request.POST.get('second')
        third = request.POST.get('third')
        changed = False
        if len(first) < 5 and len(second) < 5 and len(third) < 5:
            if third:
                interest.third_interest = third
                changed = True
            if first:
                interest.first_interest = first
                changed = True
            if second:
                interest.second_interest = second
                changed = True
            if changed:
                interest.save()
                error_info = '保存成功。'
        else:
            error_info = '输入内容太长了，别超过5个字符哦。'

    # 重定向
    return personal_interest(request, title=title, error_info=error_info)


def modify_keywords(request):
    user_id = request.session['user_id']
    user = User.objects.get(pk=user_id)
    interest = user.interest

    if request.method == 'POST':
        key_words = request.POST.get('keywords')
        title = '提示你哦：'
        if key_words and len(key_words) < 10:
            interest.key_words = key_words
            interest.save()
            error_info = '修改成功啦'
        else:
            error_info = "我猜，你要么没有输入，要么就是输入内容太长了（小于10个字符）"

    # 重定向
    return personal_interest(request, title=title, error_info=error_info)


def add_collection(request):
    user_id = request.session['user_id']
    user = User.objects.get(pk=user_id)
    label = user.label_set
    if request.method == "POST":
        data = json.loads(request.body)
        topic = data['type']
        name = data['name']
        url = data['url']
        if topic and name and url:
            label_name = label.filter(label=topic)
            if label_name:
                record = Collection(label=label_name[0], item_title=name, title_link=url)
            else:
                label = Label(user=user, label=topic)
                label.save()
                record = Collection(label=label, item_title=name, title_link=url)

            record.save()
            user.collect_count += 1
            user.save()
            request.session['collect'] = user.collect_count
        else:
            return JsonResponse({'info': '保存失败!'})

    return JsonResponse({'info': '保存成功！'})


