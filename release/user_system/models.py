from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(unique=True, max_length=20)
    age = models.CharField(max_length=10, default="老大叔")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256, default="123456")
    has_confirmed = models.BooleanField(default=False)
    # c_time = models.DateTimeField(auto_now_add=True)

    fans_count = models.IntegerField(default=0)
    read_count = models.IntegerField(default=0)
    labels = models.CharField(max_length=100, default="待探索")

    collect_count = models.IntegerField(default=0)
    code = models.IntegerField(default=000000)

    def __str__(self):
        return self.name


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"


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


class Interest(models.Model):
    user = models.OneToOneField(User)
    first_interest = models.CharField(default=None, max_length=20)
    second_interest = models.CharField(default=None, max_length=20)
    third_interest = models.CharField(default=None, max_length=20)
    key_words = models.CharField(default=None, max_length=10)

    def __str__(self):
        return self.first_interest


class History(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    title_link = models.URLField(default='www.baidu.com')
    item_title = models.CharField(default='news', max_length=50)

    def __str__(self):
        return self.item_title
