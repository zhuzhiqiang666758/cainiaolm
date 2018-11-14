from apps.article.models import *
from django import forms
from django.forms import fields
from django.forms import widgets
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('id','type','view_count','admire_count','created_user','created_at','last_update','is_recommend')

class ArticleCommentForm(forms.Form):
    content = fields.CharField(widget = widgets.Textarea(),label = '评论内容',required = False)
