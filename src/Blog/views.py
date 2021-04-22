from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Article
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import ArticleModelForm
# Create your views here.

class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <blog>/<modelmane>_list.html


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = 'articles/article_create.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all() 

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

class AboutView(View):
    template_name = 'articles/about.html'
    def get(self, request, id=None, *args, **kwargs):
        obj = get_object_or_404(Article, id=id)

        return render(request, self.template_name, {}) 