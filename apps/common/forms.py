from django.forms import Form,fields,widgets
from django import forms
from apps.common.models import *

class UserLoginForm(Form):
    username = fields.CharField(label=u'用户名')
    password = fields.CharField(widget=widgets.PasswordInput,label=u'密码')
    is_rember = forms.BooleanField(label=u'7天免登录',required=False)

class UserRegisterForm(Form):
    username = forms.CharField(label=u'用户名')
    password = forms.CharField(widget=widgets.PasswordInput(),label=u'密码')
    confirm_password = forms.CharField(widget=widgets.PasswordInput(),label=u'确认密码')
    email = forms.EmailField(label=u'电子邮箱',help_text=u'电子邮箱用于密码找回')
    nickname = forms.CharField(label=u'昵称',help_text=u'界面显示昵称代替用户名让别人记住你',required=False)
    sex = forms.ChoiceField(label=u'性别',choices=(('1','男'),('2','女')),initial='1')
    tel = forms.CharField(label=u'电话号码',min_length=11,max_length=11,required=False)
    qq = forms.CharField(label=u'QQ号码',min_length=5,required=False)
    portrait = forms.ImageField(label=u'用户头像',required=False)
    wechat_pay = forms.ImageField(label=u'微信支付', required=False)
    alipay = forms.ImageField(label=u'支付宝支付', required=False)
    wechat_fiends = forms.ImageField(label=u'添加微信好友',required=False)