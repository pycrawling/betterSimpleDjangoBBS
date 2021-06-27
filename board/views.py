# board/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Article


class AuthorRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update, delete articles """
        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseForbidden()
        return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)


class ArticleList(ListView):
    model = Article
    paginate_by = 5
    ordering = ['-id']


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    success_url = reverse_lazy('index')
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetail(DetailView):
    model = Article
    # context_object_name = 'article'


class ArticleUpdate(AuthorRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'content')
    success_url = reverse_lazy('index')


class ArticleDelete(AuthorRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('index')
