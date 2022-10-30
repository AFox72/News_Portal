from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import PostForm
from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = 'publication_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'
    permission_required = ('News.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.method == 'POST':
            post_path = self.request.META['PATH_INFO']
            if post_path == '/news/create/':
                post.post_type = 'news'
            elif post_path == '/articles/create/':
                post.post_type = 'article'

            return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'
    permission_required = ('News.change_post',)


class PostDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')
    permission_required = ('News.delete_post',)

    # Create your views here.

