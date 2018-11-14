from django.shortcuts import render,redirect
from apps.article.models import *
from apps.article.forms import *
from apps.common.views import *
# Create your views here.
from django.db.models import Q


def getArticle(request,pid):
    article = Article.objects.get(id=pid)
    comment_list = ArticleComment.objects.filter(article = article).order_by('created_at')
    comment_form = ArticleCommentForm()
    return render(request,'article/article.html',locals())

@checkLogin
def addArticle(request):
    if(request.method == 'GET'):
        obj = ArticleForm()
        type_list = Type.objects.all()
        return render(request,'article/add_article.html',locals())
    elif(request.method == 'POST'):
        obj = ArticleForm(request.POST,request.FILES)
        typeid = request.POST.get('type',None)
        if(obj.is_valid()):
            values=obj.cleaned_data
            values['type']=Type.objects.get(id=typeid)
            values['created_user']=request.user
            article = Article.objects.create(**values)
            return redirect('/article-%d'%(article.id))
        else:
            return render(request,'article/add_article.html',locals())


@checkLogin
def commentArticle(request):
    user = request.user
    id = request.GET.get('article-id')
    article = Article.objects.get(id=id)
    content = request.GET.get('content')
    comment = ArticleComment.objects.create(article=article,content=content,created_user=user)
    return redirect('/article-%s#article-comment-mao'%(id))