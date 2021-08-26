from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'slug', 'body', 'created_at', 'author')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
