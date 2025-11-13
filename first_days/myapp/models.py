from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    """文章模型"""
    title = models.CharField(max_length=200)  # 文章标题，最大长度 200
    content = models.TextField()  # 文章内容
    created_at = models.DateTimeField(default=timezone.now)  # 创建时间，默认为当前时间
    published = models.BooleanField(default=False)  # 是否发布，默认为 False
    def __str__(self):
        """返回模型的字符串表示，通常用于管理后台"""
        return self.title