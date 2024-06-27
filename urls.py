
from django.urls import path
from django.views.generic import TemplateView
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog_index, name="blog_index"),
    path('', PostListView.as_view(), name='list'),
    path('add/', PostCreateView.as_view(), name='add'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]