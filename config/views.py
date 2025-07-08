from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Imgs
from django.urls import reverse_lazy

# Create your views here.


class ImgListView(ListView):
    model = Imgs
    context_object_name = 'images'


class ImgCreateView(CreateView):
    model = Imgs
    fields = ['heading', 'image']
    success_url = reverse_lazy('img_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
