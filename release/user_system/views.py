from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import User, ConfirmString
from django.conf import settings

import datetime
import hashlib
import random


# Create your views here.

def login(request):
    if request.session.get('is_login', None):
        return redirect('/main/')
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            name = email.strip()
            user = User.objects.get(email=name)
        except(KeyError, User.DoesNotExist):
            return render(request, 'user_system/login.html', {'error_info': 'email is incorrect'})

        if hash_code(password) == user.password:

            if not user.has_confirmed:
                return render(request, 'user_system/login.html', {'error_info': 'The email has not been validated yet '})

            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            request.session['email_address'] = user.email
            request.session['age'] = user.age
            request.session['labels'] = user.labels

            request.session['fan'] = user.fans_count
            request.session['collect'] = user.collect_count

            # more info about redirect in 'https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/'
            return redirect('/main/')
        else:
            return render(request, 'user_system/login.html', {'error_info': 'password is incorrect'})

    return render(request, 'user_system/login.html')


def hash_code(s, salt='centos'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


# form a hash code as the key
def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    ConfirmString.objects.create(code=code, user=user,)
    return code


def register(request):
    if request.session.get('is_login', None):
        return redirect('/main/')

    if request.POST:
        name = request.POST.get('name')
        password = request.POST.get('password')
        age = request.POST.get('age')
        # 保证邮箱是有效的
        try:
            email = request.POST.get('email')
            validate_email(email)
        except ValidationError:
            return render(request, 'user_system/login.html', {'error_info': 'Email is not valid '})

        # 确保email是unique
        anonymous = User.objects.filter(email=email)
        if anonymous:
            return render(request, 'user_system/login.html', {'error_info': 'The email you filled in is registered already'})

        # 确保name是unique
        anonymous = User.objects.filter(name=name)
        if anonymous:
            return render(request, 'user_system/login.html', {'error_info': 'The name you filled in is registered already'})

        # 创建一个新用户
        user = User(name=name, email=email, age=age, password=hash_code(password))
        user.save()

        code = make_confirm_string(user)
        send_email(email, code)
        return render(request, 'user_system/login.html', {'error_info': '请前往注册邮箱，进行邮件确认！'})

    return render(request, 'user_system/login.html', {'error_info': 'failed'})


def send_code(request):
    code = ""
    for i in range(0, 6):
        digit = int(random.random() * 10)
        code += str(digit)

    message = "Failed"
    if request.POST:
        try:
            code_email = request.POST.get('email')
            validate_email(code_email)
        except ValidationError:
            return render(request, 'user_system/login.html', {'error_info': 'Email is not valid '})

        from django.core.mail import EmailMultiAlternatives
        subject = '来自的今日发布的密码修改提示！'
        text_content = '你的验证码是 ' + code + '!'
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [code_email])
        msg.send()
        message = "邮件已发送 "

        # 对比  save（）和 update（）：https://blog.csdn.net/luojie140/article/details/78052408
        User.objects.filter(email=code_email).update(code=code)

        return render(request, 'user_system/login.html', {'error_info': message, 'user_email': code_email})

    return render(request, 'user_system/login.html', {'error_info': message})

def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = '欢迎访问今日发布！'

    text_content = '来自 今日发布 的测试邮件, 欢迎访问！'

    html_content = '''
                    欢迎来到 <a href="http://{}/index/user_confirm/?code={}" target=blank>今日发布</a>，
                    来自今日发布的测试邮件, 欢迎访问！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为 {} 天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def forget_password(request):
    error_info = "Failed"
    if request.POST:
        code_email = request.POST.get('user_email')
        check_code = request.POST.get('code')
        if not check_code:
            error_info = "你的验证码没有输入哦"

        else:
            user = User.objects.get(email=code_email)
            code = user.code
            if code == int(check_code):
                password = request.POST.get('password')
                if len(password) < 6:
                    error_info = "密码太短啦，长一点好不洛"

                else:
                    user = User.objects.get(email=code_email)
                    user.password = hash_code(password)
                    user.save()
                    error_info = '密码重置完成！'
            else:
                error_info = '验证码不对呢'
    return render(request, 'user_system/login.html', {'error_info': error_info})


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'user_system/confirm.html', locals())

    c_time = confirm.c_time

    # datetime.datetime.now is not timezone aware. more info: http://blog.csdn.net/qq_25420115/article/details/53149669
    from django.utils import timezone
    now = timezone.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'user_system/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'user_system/confirm.html', locals())


def logout(request):
    if request.session.get('is_login', None):
        request.session.flush()

    return redirect("/main/")


def add_label(request):
    if request.POST:
        label = request.POST.get('label')
        user_email = request.session['email_address']
        user = User.objects.get(email=user_email)
        user.labels = user.labels + '/' + label
        user.save()
        request.session['labels'] = user.labels.split('/')

    return render(request, 'user_system/personal_info.html')


def delete_label(request):
    pass
