from django.shortcuts import render
from django.views import generic
from .models import Uploads

# Create your views here.
class PostList(generic.ListView):
    queryset = Uploads.objects.all()
    template_name = "news/index.html"
    paginate_by = 6