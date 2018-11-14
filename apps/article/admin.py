from django.contrib import admin
from apps.article.models import *
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','type','title','view_count','admire_count','created_user','created_at','last_update','is_recommend']
    list_display_links = ['id','type','title','view_count','admire_count','created_user','created_at','last_update']
    list_editable = ['is_recommend']

    class Media:
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )

@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['id','article','created_user','created_at','last_update']
    list_display_link = ['id','article','created_user','created_at','last_update']
    class Media:
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )