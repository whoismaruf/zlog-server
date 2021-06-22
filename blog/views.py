from rest_framework import generics
from blog.models import Blog
from django.contrib.auth.models import User
from blog.serializers import BlogSerializer
from root.permissions import AuthorPermission


class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AuthorPermission,)


class AuthorsBlogView(generics.ListAPIView):
    def get_queryset(self):
        return Blog.objects.all().filter(author=self.request.user)
    serializer_class = BlogSerializer
    permission_classes = (AuthorPermission,)