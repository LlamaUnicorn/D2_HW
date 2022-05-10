from django.shortcuts import render
from datetime import datetime

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm

# Create your views here.


class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'singular_news.html'
    context_object_name = 'singular_news'


class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'
    permission_required = ('news.add_post', )

    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     post.categoryType = 'NW'
    #     return super().form_valid(form)

#
# class ArticleCreate(CreateView):
#     # Указываем нашу разработанную форму
#     form_class = PostForm
#     # модель товаров
#     model = Post
#     # и новый шаблон, в котором используется форма.
#     template_name = 'article_edit.html'
#
#     def form_valid(self, form):
#         post = form.save(commit=False)
#         post.categoryType = 'AR'
#         return super().form_valid(form)


class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    permission_required = ('news.change_post', )


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(NewsList):
    form_class = PostForm
    model = Post
    template_name = 'news_search.html'
    success_url = reverse_lazy('news_search')


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'


class CategoryList(ListView):
    model = Category  # указываем модель, объекты которой мы будем выводить
    template_name = 'category.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'categorys'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    paginate_by = 5


@login_required
def subscribe_me(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if category not in user.category_set.all():
        category.subscribers.add(user)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))

@login_required
def unsubscribe_me(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if category in user.category_set.all():
        category.subscribers.remove(user)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))