from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/grow/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=15) #제목
    hook_text = models.CharField(max_length=100) #소주제
    detail = models.TextField(max_length=1000) #자세한 내용
    created_at = models.DateTimeField() #작성날짜

    image = models.ImageField(upload_to='grow/images/%Y/%m/%d', blank=True) #이미지
    file_upload = models.FileField(upload_to='grow/files/%Y/%m/%d', blank=True) #첨부파일

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/grow/{self.pk}/'


