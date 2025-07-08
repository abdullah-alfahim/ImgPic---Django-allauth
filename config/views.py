from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
    

class UserImgListView(ListView):
    model = Imgs
    context_object_name = 'image'
    template_name = 'config/user_images.html'

    def get_queryset(self):
        return Imgs.objects.filter(user=self.request.user).order_by('-date')

class ImgUpdateView(UpdateView):
    model = Imgs
    fields = ['heading', 'image']
    success_url = reverse_lazy('img_list')


class ImgDeleteView(DeleteView):
    model = Imgs
    success_url = reverse_lazy('img_list')
