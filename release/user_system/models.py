from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(unique=True, default=0)
    name = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)

    fans_count = models.IntegerField(default=0)
    read_count = models.IntegerField(default=0)
    collect_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Fan(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        # 这个参数我们可以不设置，Django会默认以模型的小写作为反向关联名
        related_name='all_fans',
    )

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



