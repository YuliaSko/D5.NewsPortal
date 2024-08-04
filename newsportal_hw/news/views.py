import datetime

from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm


class PostsList(ListView):
    model = Post
    ordering = '-date_post'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 3


class ItemDetail(DetailView):
    model = Post
    template_name = 'item.html'
    context_object_name = 'item'


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    ordering = '-date_post'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        today = datetime.date.today()
        count_posts = Post.objects.filter(author=post.author, date_post__date=today).count()

        if self.request.path == '/news/articles/create/':
            post.type_post = 'AR'

        if count_posts > 3:
            return render(self.request, 'limit_posts.html', {'author': post.author})

        post.save()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    context_object_name = 'edit'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')
    context_object_name = 'delete'


class CategoryPostList(PostsList):
    model = Post
    template_name = 'category_post_list.html'
    context_object_name = 'category_posts_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(categories=self.category).order_by('-date_post')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribes.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribes.add(user)

    massage = 'Вы подписались на рассылку категории'
    return render(request, 'subscribe.html', {'category': category, 'massage': massage})


