from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Uploads(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    journalist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_uploads")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    
class Commenting(models.Model):
    comment = models.ForeignKey(Uploads, on_delete=models.CASCADE, related_name="comments")
    journalist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    authorised = models.BooleanField(default=False)