from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'pk={self.pk}, title={self.title}, created_at={self.created_at}, updated_at={self.updated_at}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'