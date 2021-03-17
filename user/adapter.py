from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import LikelionUser


class LikelionAccountAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        return True

    def save_user(self, request, sociallogin, form=None):
        user = super(LikelionAccountAdapter, self).save_user(request, sociallogin, form)
        return LikelionUser.objects.get_or_create_user(user.pk, sociallogin.account.extra_data)
