from django.db import models
from django.urls import reverse

# Create your models here.
class Portfolio(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title