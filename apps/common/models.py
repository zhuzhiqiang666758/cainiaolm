from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


#类别表
class Category(models.Model):
    name = models.CharField(verbose_name=u'类别名称', max_length=10,unique=True)
    remark = models.CharField(verbose_name=u'备注',max_length=100,blank=True,null=True,default='')
    class Meta:
        db_table='common_type'
        verbose_name = u'类别表'
    def __str__(self):
        return self.name


#类型表
class Type(models.Model):
    category = models.ForeignKey(verbose_name=u'所属类别', to=Category)
    name = models.CharField(verbose_name=u'分类名称',max_length=10,unique=True)
    remark = models.CharField(verbose_name=u'备注',max_length=100,blank=True,null=True,default='')
    class Meta:
        db_table = 'common_category'
        verbose_name = u'类型表'
    def __str__(self):
        return self.name
#用户表
class User(AbstractUser):
    username = models.CharField(verbose_name=u'用户名',primary_key=True,max_length=20)
    nickname = models.CharField(verbose_name=u'昵称', max_length=10,unique=True)
    email = models.EmailField(verbose_name=u'电子邮箱',help_text=u'填写电子邮箱用于密码找回',unique=True)
    sex = models.CharField(max_length=2,choices=(('1', '男'), ('2', '女')), default='1',
                              verbose_name='性别')
    tel = models.IntegerField(verbose_name=u'联系电话', blank=True, null=True)
    qq = models.IntegerField(verbose_name=u'QQ', blank=True, null=True)
    portrait = models.ImageField(verbose_name=u'头像',blank=True,null=True)
    wechat_pay = models.ImageField(verbose_name=u'微信支付',upload_to='pay/wechat/%Y/%m',blank=True,null=True,help_text=u'微信支付')
    alipay = models.ImageField(verbose_name=u'支付宝支付',upload_to='pay/alipay/%Y/%m',blank=True,null=True,help_text=u'支付宝支付')
    wechat_fiends = models.ImageField(verbose_name=u'微信好友',upload_to='wechat/%Y/%m',blank=True,null=True,help_text=u'添加微信好友')
    class Meta:
        db_table='common_user'
        verbose_name=u'用户表'
    def __str__(self):
        return self.username

#友情链接
class FriendlyLink(models.Model):
    title = models.CharField('标题', max_length=50)
    link = models.URLField('链接', max_length=50, default='')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'

# Banner(轮播图模型)
class Banner(models.Model):
    title = models.CharField('标题', max_length=50)
    cover = models.ImageField('轮播图', upload_to='banner/%Y/%m')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=50,default='')
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型", choices=(("register",u"注册"),("forget","找回密码"), ("update_email","修改邮箱")), max_length=30)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        # 复数
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)