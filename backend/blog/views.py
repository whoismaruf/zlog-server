from rest_framework import generics
from blog.models import Blog
from blog.serializers import BlogSerializer
from api.permissions import AuthorPermission


class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AuthorPermission,)
