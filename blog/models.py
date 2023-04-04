from django.db import models
from django.contrib.auth.models import User
import os

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)   
    
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'
    

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)   
    
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'
    
    class Meta:
        verbose_name_plural = 'Categories'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    head_image = models.ImageField(blank=True, upload_to='blog/images/%Y/%m/%d')
    # head_image = models.ImageField(blank=True)
    
    file_upload = models.FileField(blank=True, upload_to='blog/files/%Y/%m/%d')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    
    # tag를 지운다고 해서 post 에 영향이 갈 필요가 없다. 기본으로 null=True
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'pk={self.pk}, title={self.title}, created_at={self.created_at}, author={self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    


