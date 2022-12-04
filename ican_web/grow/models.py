from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=15) #제목
    hook_text = models.CharField(max_length=100) #소주제
    detail = models.TextField(max_length=1000) #자세한 내용
    created_at = models.DateTimeField() #작성날짜

    image = models.ImageField(upload_to='grow/images/%Y/%m/%d', blank=True) #이미지
    def __str__(self):
        return f'{self.created_at} {self.title}'

    def get_absolute_url(self):
        return f'/grow/post-{self.pk}/'