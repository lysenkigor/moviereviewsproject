from django.shortcuts import render

# Create your views here.
from news.models import News


def news(request):
    news = News.objects.all().order_by('-date')
    context = {'news': news}
    return render(request, 'news/news.html', context=context)
