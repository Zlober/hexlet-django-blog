from django.forms import ModelForm
from .models import Article


from django import forms


class ArticleFrom(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
