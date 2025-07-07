from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_field
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import redirect
from django.urls import reverse

class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
       
        pass

    def save_user(self, request, sociallogin, form=None):
       
        user = sociallogin.user
        extra_data = sociallogin.account.extra_data

     
        user_field(user, 'first_name', extra_data.get('given_name', ''))
        user_field(user, 'last_name', extra_data.get('family_name', ''))
        if not user.email and extra_data.get('email'):
            user.email = extra_data['email']
            user.email_verified = True
     
        user = super().save_user(request, sociallogin, form)

        if 'picture' in extra_data and user.profile:
            user.profile.google_profile_picture_url = extra_data['picture']
            user.profile.save()

        return user

    def socialaccount_updated(self, request, sociallogin):
      
        user = sociallogin.user
        extra_data = sociallogin.account.extra_data

        user_field(user, 'first_name', extra_data.get('given_name', user.first_name))
        user_field(user, 'last_name', extra_data.get('family_name', user.last_name))
        if extra_data.get('email') and user.email != extra_data['email']:
            user.email = extra_data['email']
            user.email_verified = True
        user.save()

        if 'picture' in extra_data and user.profile:
            if user.profile.google_profile_picture_url != extra_data['picture']:
                user.profile.google_profile_picture_url = extra_data['picture']
                user.profile.save()