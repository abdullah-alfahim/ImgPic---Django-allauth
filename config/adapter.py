from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return settings.LOGIN_REDIRECT_URL