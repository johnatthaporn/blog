from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post

# Create your views here.
def blog_index(request):
    return render(request, 'blog/blog_index.html')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(UpdateView):
    model = Post
    fields = ['title', 'body', 'author']
    template_name = 'blog/post_detail.html'