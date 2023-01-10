from django.shortcuts import render
from django.views import View



class IndexArticle(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'article/index.html', context={'name': 'Article'})
