from django.conf.urls import url
from . import views

app_name = 'display'
urlpatterns=[
    url(r'^$', views.index, name="index"),
    url(r'^today/recommendation', views.recommendation, name="recommendation"),
    url(r'^(?P<category>[\u4e00-\u9fa5]+)/$', views.category, name='category'),
    url(r'^search/', views.search, name='search'),
    # url(r'^today/interest', views.interest, name="interest"),
    # url(r'^today/hit', views.hit, name="interest"),

    url(r'^personal_info/', views.personal_info, name='personal_info'),
    url(r'^personal_interest/', views.personal_interest, name='personal_interest'),
    url(r'^personal_warehouse/', views.personal_warehouse, name='personal_warehouse'),
    url(r'^personal_interest/', views.personal_interest, name='personal_interest'),
    url(r'^modify_interest/', views.modify_interest, name='modify_interest'),
    url(r'^modify_keywords/', views.modify_keywords, name='modify_keywords'),
    url(r'^add_collection/', views.add_collection, name='add_collection'),
    url(r'^(?P<url>[\s\S]*)', views.click, name='click'),

]
