from django.db import models
from django.utils import timezone
import datetime
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

class question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text