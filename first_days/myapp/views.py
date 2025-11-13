from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.



def home(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    # 将文章列表传递给模板
    return render(request, 'myapp/home.html', {'articles': articles})