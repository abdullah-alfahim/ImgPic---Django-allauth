from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    google_profile_picture_url = models.URLField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        name = self.user.get_full_name() or self.user.username or self.user.email
        return f'{name} Profile'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save() 


class Imgs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images')
    heading = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.user.username} - {self.heading} ({self.date})"
    
    def get_absolute_url(self):
        return reverse('img_list', kwargs={'pk': self.pk})