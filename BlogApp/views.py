from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *

def main_view(request):
    template = loader.get_template('index.html')

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
        
    return HttpResponse(template.render(context, request))

def tag_view(request, tag_name):
    template = loader.get_template('index.html')

    articles = Article.objects.filter(tags__name=tag_name)
    context = {
        'articles': articles,
    }
        
    return HttpResponse(template.render(context, request))

def post_view(request, post_id):
    template = loader.get_template('article.html')
    article = Article.objects.get(id=post_id)

    context = {
        'article': article,
    }
    return HttpResponse(template.render(context, request))

def add_post_view(request):
    template = loader.get_template('add_article.html')

    if request.method == "POST":
        print(f"{request.POST=}")
        print(f"{request.FILES=}")
        print(f"{request.POST.getlist('tags')=}")
        author = Author.objects.get(user=request.user)
        title = request.POST['title']
        text = request.POST['text']

        if 'image' in request.FILES:
            img = request.FILES['image']
            new_article = Article(author=author, title=title, text=text, image=img)
        else:
            new_article = Article(author=author, title=title, text=text)
        new_article.save()
        
        for tag_name in request.POST.getlist('tags'):
            print(tag_name)
            tag = Tag.objects.get(name=tag_name)
            new_article.tags.add(tag)

    context = {
        'tags': Tag.objects.all()
    }
    return HttpResponse(template.render(context, request))

def delete_post_view(request, post_id):
    if request.user.author.role == 'admin':
        article = Article.objects.get(id=post_id)
        article.delete()
    return redirect('main')

@login_required
def add_comment_view(request, post_id):
    article = Article.objects.get(id=post_id)
    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            comment = Comment(article=article, author=request.user.author, text=text)
            comment.save()
    return redirect('post', post_id=article.id)

def delete_comment_view(request, post_id, comment_id):
    if request.user.author.role == 'admin':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('post', post_id=post_id)