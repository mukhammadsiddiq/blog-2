from .views import ArticleListView, ArticleDetailView, ArticleDeleteView, ArticleEditView
from django.urls import path

urlpatterns = [
    path('articles/<int:pk>/edit', ArticleEditView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleListView.as_view(), name='article_list'),
]