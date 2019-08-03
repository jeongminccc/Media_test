from django.db import models
from django.urls import reverse
import os
from uuid import uuid4
from django.utils import timezone

# Create your models here.
class Portfolio(models.Model):
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def date_upload_to(instance, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        plus_date = timezone.now().strftime('%H%M%S')
        # 결합 후 return
        return '/'.join([
            ymd_path,
            uuid_name + plus_date + extension,
        ])
    
    image = models.ImageField(upload_to=date_upload_to)
    
