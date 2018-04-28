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

]
