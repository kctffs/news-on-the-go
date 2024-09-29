from django.shortcuts import render
from django.views import generic
from .models import Uploads

# Create your views here.
class PostList(generic.ListView):
    queryset = Uploads.objects.filter(status=1)
    template_name = "news/article_list.html"