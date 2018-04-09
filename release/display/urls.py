from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name="index"),
    url(r'^today/recommendation', views.recommendation, name="recommendation"),
    # url(r'^today/interest', views.interest, name="interest"),
    # url(r'^today/hit', views.hit, name="interest"),

]