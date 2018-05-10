from django.db import models
from time import timezone
import datetime

# python manage.py makemigrations ---record
# python manage.py migrate  --- work on database
# Create your models here.


class Item(models.Model):
    item_id = models.CharField(max_length=200, unique=True)
    item_title = models.CharField(max_length=50, default='news')
    item_type = models.CharField(max_length=10, default='最新')
    title_link = models.URLField()
    cut_url = models.URLField()
    collect_time = models.DateField()
    author = models.CharField(max_length=20, default='unknown author')

    item_source = models.CharField(max_length=20, default='unknown source')

    category = models.CharField(max_length=20, default='unknown category')

    like_count = models.IntegerField(default=0)

    view_count = models.IntegerField(default=0)

    share_count = models.IntegerField(default=0)

    def __str__(self):
        return self.item_id

    # 判断该消息是不是新消息
    def pub_in_2_days(self):

        return timezone - self.collect_time <= datetime.timedelta(days=2)


class HitItem(models.Model):
    item_id = models.CharField(max_length=200, unique=True)
    item_title = models.CharField(max_length=50, default='news')
    item_type = models.CharField(max_length=10, default='最新')
    title_link = models.URLField()

    rank = models.IntegerField(default=0)
    collect_time = models.DateField()

    item_source = models.CharField(max_length=20, default='unknown source')

    like_count = models.IntegerField(default=0)

    view_count = models.IntegerField(default=0)

    share_count = models.IntegerField(default=0)

    def __str__(self):
        return self.item_id


class Images(models.Model):
    item_id = models.IntegerField(default=0)
    item_title = models.CharField(max_length=20, default='图片')
    item_url = models.URLField(default='http://img.ivsky.com/img/bizhi/li/201602/04/nba-001.jpg')
    collect_time = models.DateField()
    item_source = models.CharField(max_length=10, default=20)
    like_count = models.IntegerField(default=0)
    category = models.CharField(max_length=10,default='你猜')

