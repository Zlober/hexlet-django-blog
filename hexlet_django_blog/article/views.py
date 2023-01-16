from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from hexlet_django_blog.article.models import Article
from .forms import ArticleFrom
from django.contrib import messages


class IndexArticle(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={'articles': articles})


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'article/show.html', context={'article': article})


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleFrom()
        return render(request, 'article/create.html', context={'form': form})


    def post(self, request, *args, **kwargs):
        form = ArticleFrom(request.POST)
        if form.is_valid():
            messages.success(request, 'The article has been added successfully.')
            form.save()
            return redirect('article')
        messages.error(request, 'Please correct the following errors:')
        return render(request, 'article/create.html', context={'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleFrom(instance=article)
        return render(request, 'article/update.html', context={'article_id': article_id, 'form': form})


    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleFrom(request.POST, instance=article)
        if form.is_valid():
            messages.success(request, 'The article has been updated successfully.')
            form.save()
            return redirect('article')
        return render(request, 'article/update.html', {'article_id': article_id, 'form': form})


class ArticleDelete(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('article')