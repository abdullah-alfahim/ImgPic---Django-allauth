
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views import ImgListView, ImgCreateView, ImgUpdateView, ImgDeleteView, UserImgListView
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', ImgListView.as_view(), name='img_list'),
    path('add/', ImgCreateView.as_view(), name='img_add'),
    path('update/<int:pk>', ImgUpdateView.as_view(), name='img_update'),
    path('delete/<int:pk>', ImgDeleteView.as_view(), name='img_delete'),
    path('profile/', UserImgListView.as_view(), name='user_img_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 