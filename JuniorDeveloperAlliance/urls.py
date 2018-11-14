"""JuniorDeveloperAlliance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apps.common.views import *
from apps.article.views import *
from JuniorDeveloperAlliance import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/',login),
    url(r'register',register),
    url(r'logout',logout),
    url(r'about-me/',getAboutMe),
    url(r'^base/',base),
    url(r'^$', index),
    url(r'^article-(?P<pid>\d+)',getArticle),
    url(r'^add-article',addArticle),
    url(r'^getType',getType),
    url(r'^comment-article', commentArticle),

    #富文本编辑器Kindeditor
    url(r'^admin/upload/(?P<dir_name>[^/]+)$',upload_image,name='upload_image'),
    url(r'uploads/(?P<path>.*)$',serve,
        {'document_root':settings.MEDIA_ROOT,}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
