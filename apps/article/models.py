from django.db import models

from apps.common.models import *
# Create your models here.

class Article(models.Model):
    id = models.AutoField(verbose_name=u'编号',primary_key=True)
    type = models.ForeignKey(verbose_name=u'文章类型',to=Type)
    title = models.CharField(verbose_name='文章标题',max_length=100)
    content = models.TextField(verbose_name=u'文章正文',default='')
    cover = models.ImageField(verbose_name=u'文章封面',blank=True,null=True,upload_to='cover/%Y/%m',help_text=u'上传个性图片，让您的文章更受欢迎')
    tags = models.CharField(verbose_name=u'文章标签',max_length=15,help_text=u'请提取文章的关键字，方便文章被找到')
    view_count = models.IntegerField(verbose_name=u'访问次数',default=0)
    admire_count = models.IntegerField(verbose_name=u'点赞次数',default=0)
    created_user = models.ForeignKey(verbose_name=u'创建人', to=User, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=u'创建时间',auto_now_add=True)
    last_update = models.DateTimeField(verbose_name=u'最后修改时间',auto_now=True)
    is_recommend = models.BooleanField(verbose_name=u'是否推荐',default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name=u'文章表'
        db_table='article_articel'
    def colored_name(self):
        return format_color('<span style="color: #{};">{} {}</span>',
                           self.color_code,
                           self.view_count,
                           self.admire_count)


class ArticleComment(models.Model):
    id = models.AutoField(verbose_name=u'编号',primary_key=True)
    article = models.ForeignKey(verbose_name=u'对那个文章的评论',to=Article,blank=True,null=True)
    content = models.TextField(verbose_name=u'评论内容',default='')
    created_user = models.ForeignKey(verbose_name=u'评论者', to=User, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    last_update = models.DateTimeField(verbose_name=u'最后修改时间', auto_now=True)
    def __str__(self):
        return self.article.title
    class Meta:
        verbose_name=u'文章评论'
        db_table='article_comment'
