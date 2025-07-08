from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Imgs

# Create your views here.


class ImgListView(ListView):
    model = Imgs
    context_object_name = 'images'


class ImgCreateView(CreateView):
    model = Imgs
    fields = ['heading', 'image']
