from django.shortcuts import render,redirect
from JuniorDeveloperAlliance.settings import *
from apps.article.models import *
from apps.common.forms import *
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.core import serializers
# Create your views here.

def globaPara(request):
    site_name = SITE_NAME
    meta_keywords = META_KEYWORDS
    meta_desp = META_DESCRIPTION

    category_list = Category.objects.all()
    type_list = Type.objects.all()

    navbar_dict = {}
    for category in category_list:
        type_list = Type.objects.filter(category=category)
        print(type_list)
        navbar_dict[category.name] = type_list
    print(navbar_dict)
    return locals()

def getType(request):
    categoryid = request.GET.get('categoryid')
    print(categoryid)
    type_list = Type.objects.filter(category__id = categoryid)
    type_json = serializers.serialize('json',type_list)
    print(type_json)
    return HttpResponse(type_json)


def base(request):
    return render(request, 'common/base.html')

def index(request):
    article_list = Article.objects.all().order_by('-created_at')[0:10]
    return render(request,'common/index.html',locals())

def checkLogin(func):
    def inner(request,*args,**kwargs):
        next = request.get_full_path()
        user = request.user
        if(user.is_authenticated):
            return func(request,*args,**kwargs)
        else:
            login_form = UserLoginForm()
            return render(request,'common/login.html',{'login_form':login_form,'next':next})
    return inner

def login(request):
    if(request.method == 'GET'):
        login_form = UserLoginForm()
        return render(request,'common/login.html',locals())
    elif(request.method == 'POST'):
        error_message = ''
        next = request.POST.get('next')
        if(next == ''):
            next = '/'
        obj = UserLoginForm(request.POST)
        if(obj.is_valid()):
            values = obj.cleaned_data
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,password=password)
            if(user is not None):
                if(user.is_active):
                    auth.login(request,user)
                    return redirect(next)
            else:
                error_message='用户名密码错误，请重新输入'
                return render(request,'common/login.html',{'login_form':obj,'error_message':error_message,'next':next})
        else:
            error_message = '输入有误，请检查输入是否符合要求'
            return render(request,'common/login.html',{'login_form':obj,'error_message':error_message,'next':next})
def logout(request):
    next = request.get_full_path()
    auth.logout(request)
    return redirect('/')
def register(request):
    error_message = ''
    if(request.method == 'GET'):
        obj = UserRegisterForm()
        return render(request,'common/register.html',locals())
    elif(request.method == 'POST'):
        obj = UserRegisterForm(request.POST,request.FILES)
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')
        if(password != confirm_password):
            error_message = '两次输入的密码输入不一致'
            obj.password=''
            obj.confirm_password=''
            context = {}
            context['obj']=obj
            context['error_message']=error_message
            return render(request,'common/register.html',context)
        elif(obj.is_valid()):
            values=obj.cleaned_data
            del values['confirm_password']
            print(values)
            user = User.objects.create(**values)
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'common/register.html',locals())




def getAboutMe(request):
    return render(request,'common/about_me.html')




####################################富文本编辑器图片上传###############################
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
import uuid
import json
import datetime as dt
@csrf_exempt
def upload_image(request, dir_name):
    result = {'error': 1, 'message': '上传出错'}
    files = request.FILES.get('imgFile', None)
    if files:
        result = image_upload(files, dir_name)
    return HttpResponse(json.dumps(result),
                        content_type='application/json')
# 目录创建
def upload_generation_dir(dir_name):
    # print dir_name, '----dir_name'
    today = dt.datetime.today()
    dir_name = dir_name + '/%d/%d/' % (today.year, today.month)
    if not os.path.exists(settings.MEDIA_ROOT + dir_name):
        os.makedirs(settings.MEDIA_ROOT + dir_name)
    return dir_name
# 图片上传
def image_upload(files, dir_name):
    # 允许上传的类型
    allow_suffix = ['jpg', 'png', 'jpeg', 'git', 'bmp']
    file_suffix = files.name.split('.')[-1]
    if file_suffix not in allow_suffix:
        return {'error': 1, 'message': '图片格式不正确'}
    relative_path_file = upload_generation_dir(dir_name)
    # print relative_path_file, '-----relative_path_file'
    path = os.path.join(settings.MEDIA_ROOT, relative_path_file)
    # print path, '----------path'
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = str(uuid.uuid1()) + '.' + file_suffix
    path_file = os.path.join(path, file_name)
    file_url = settings.MEDIA_URL + relative_path_file + file_name
    open(path_file, 'wb').write(files.file.read())
    return {'error': 0, 'url': file_url}

# #################################富文本编辑器文件上传################################################################