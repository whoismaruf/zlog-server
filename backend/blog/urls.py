from django.urls import path
from blog.views import BlogDetailView, BlogView, AuthorsBlogView


urlpatterns = [
    path('', BlogView.as_view(), name='blog_view'),
    path('my/', AuthorsBlogView.as_view(), name='authors_blog_view'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]
