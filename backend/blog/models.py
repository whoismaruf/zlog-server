from django.http import request
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Blog(models.Model):
    ''' Blog Models to save blogs by user. \n
    
    '''
    title = models.CharField(max_length=500)
    body = models.TextField()
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
