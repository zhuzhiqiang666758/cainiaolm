from django.contrib import admin

# Register your models here.
from apps.common.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','remark']
    list_display_links = ['name','remark']
    class Media:
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['category','name','remark']
    list_display_links = ['category','name','remark']
    class Media:
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','nickname','sex']
    list_display_link = ['username','nickname','sex']
    search_fields = ['username','nickname']

    class Media:
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )