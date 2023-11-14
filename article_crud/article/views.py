from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
import sys

# Create your views here.

def index(request):
    articles = Article.objects.all()

    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArticleForm()
    else:
        form = ArticleForm()


    return render(request, 'index.html', {
        'articles': articles,
        'form': form
    })
