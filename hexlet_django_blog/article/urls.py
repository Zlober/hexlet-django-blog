from django.urls import path
from hexlet_django_blog.article.views import IndexArticle, ArticleView, ArticleFormCreateView, ArticleFormEditView, ArticleDelete


urlpatterns = [
    path('', IndexArticle.as_view(), name='article'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:article_id>', ArticleView.as_view(), name='show_article'),
    path('create/', ArticleFormCreateView.as_view(), name='article_create'),
    path('<int:id>/delete/', ArticleDelete.as_view(), name='article_delete')
]
