from django.shortcuts import render
from . models import Articles

# Create your views here.
def index(request):
    all_articles = Articles.objects.all
    return render(request, 'index.html', {'all': all_articles})

def article(request):
    return render(request, 'article.html')
