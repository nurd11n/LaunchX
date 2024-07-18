from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.core.exceptions import ImmediateHttpResponse
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        
        username = data.get('username') or data.get('email').split('@')[0]
        original_username = username
        counter = 1

        while User.objects.filter(username=username).exists():
            username = f"{original_username}{counter}"
            counter += 1

        user.username = username
        return user

    def save_user(self, request, sociallogin, form=None):
        user = super(SocialAccountAdapter, self).save_user(request, sociallogin, form)
        user.is_active = True  
        user.save()
        return user
    