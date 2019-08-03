from django.conf import settings
from django.db import models
import os
from uuid import uuid4
from django.utils import timezone


class TimeStampedModel(models.Model):
    """Base Model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    """ Post Model """
    title = models.CharField(max_length=140)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='post'
        )

    def date_upload_to(instance, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        # 길이 32 인 uuid 값 임의로 생성
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        # image upload한 시간을 저장되는 파일명에 추가
        plus_date = timezone.now().strftime('-%H%M%S')
        # 결합 후 return
        return '/'.join([
            'post/' +
            ymd_path,
            'DesAI' + plus_date + uuid_name + extension, # 합쳐서 파일이름 생성
        ])

    image = models.ImageField(upload_to=date_upload_to, blank=False, null=True)
    context = models.TextField(max_length=200)
    
    @property
    def comment_count(self):
        return self.comments.count()
    
    @property
    def summary(self):
        return self.text[:50]

    def __str__(self):
        return f'{self.title}-{self.creator}'

    class Meta:
        ordering = ['-created_at']

class Result(TimeStampedModel):
    """ Result Model """
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='result'
    )
    title = models.CharField(max_length=140)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='result'
        )

    def date_upload_to(instance, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        # 길이 32 인 uuid 값 임의로 생성
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        # image upload한 시간을 저장되는 파일명에 추가
        plus_date = timezone.now().strftime('-%H%M%S')
        # 결합 후 return
        return '/'.join([
            'result/' +
            ymd_path,
            'DesAI' + plus_date + uuid_name + extension, # 합쳐서 파일이름 생성
        ])

    image = models.ImageField(upload_to=date_upload_to, blank=False, null=True)
    context = models.TextField(max_length=200)
    
    @property
    def summary(self):
        return self.text[:50]

    def __str__(self):
        return f'{self.title}-{self.creator}'

    class Meta:
        ordering = ['-created_at']

        
class Comment(TimeStampedModel):
    """ Comment Model """
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='comments'
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
    )
    text = models.TextField()
    
    def __str__(self):
        return f'{self.post}-{self.creator}'

    class Meta:
        ordering = ['-created_at']    
        
