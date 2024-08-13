from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.


class ArticleListView(ListView):
    template_name = 'article_list.html'
    model = Articles


class ArticleDetailView(DetailView):
    template_name = 'detailArticle.html'
    model = Articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the ProfileInfo object (assuming there is only one)
        article = Articles.objects.first()  # Adjust query as needed
        context['article'] = article
        return context


class ArticleEditView(UpdateView):
    template_name = 'editArticle.html'
    model = Articles
    fields = ('title', 'summary', 'body', 'image')


class ArticleDeleteView(DeleteView):
    template_name = 'deleteArticle.html'
    model = Articles
    success_url = reverse_lazy('article_list')
