from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article_list.html'
    model = Articles


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detailArticle.html'
    model = Articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the ProfileInfo object (assuming there is only one)
        article = Articles.objects.first()  # Adjust query as needed
        context['article'] = article
        return context


class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'editArticle.html'
    model = Articles
    fields = ('title', 'summary', 'body', 'image')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'deleteArticle.html'
    model = Articles
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'newArticle.html'
    model = Articles
    fields = ('title', 'summary', 'body', 'image')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(self)

    def test_func(self):
        return self.request.user.is_superuser

