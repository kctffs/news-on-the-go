from django.shortcuts import render
from django.views import generic
from .models import Uploads

# Create your views here.
class UploadsList(generic.ListView):
    model = Uploads