from django.db import models
from time import timezone
import datetime

# python manage.py makemigrations ---record
# python manage.py migrate  --- work on database
# Create your models here.


class Item(models.Model):
    item_id = models.IntegerField(default=0)
    item_title = models.CharField(max_length=50, default='news')
    item_type = models.CharField(max_length=5, default='最新')
    title_link = models.URLField()
    cut_url = models.URLField()
    # 每当对象被创建时，自动设为当前日期，常用于保存创建日期(注意，它是不可修改的)
    collect_time = models.DateField(auto_now_add=True)

    source = models.CharField(max_length=20)

    CATA_CHOICES = {
        ('news', '时政'),
        ('entertain', '娱乐'),
        ('sport', '体育'),
        ('jobs', '职位'),
        ('music', '音乐'),
        ('funs', '段子'),
        ('military', '军事'),
        ('bonus', '福利'),
    }

    like = models.IntegerField(default=0)

    view = models.IntegerField(default=0)

    share = models.IntegerField(default=0)

    def __str__(self):
        return self.item_id

    # 判断该消息是不是新消息
    def pub_in_2_days(self):

        return timezone - self.collect_time <= datetime.timedelta(days=2)


