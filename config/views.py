from django.shortcuts import render
from django.views.generic import ListView
from .models import Imgs

# Create your views here.


class ImgListView(ListView):
    model = Imgs
