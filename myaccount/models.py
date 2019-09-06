from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django_mysql.models import ListCharField


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    org = models.CharField('Organization', max_length=128, blank=True)
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    line_api_key = models.CharField('LINE api key', max_length=100, blank=True)
    email_address = models.CharField('Email address', max_length=100, blank=True)
    mod_date = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return f"{self.user}'s profile"


class UserKeyword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='keyword')
    keyword = models.CharField(max_length=30,blank=True)

    class Meta:
        verbose_name = 'User Keyword'

    def __str__(self):
        return f"{self.user} {self.keyword}"


@receiver(user_signed_up)
def user_signed_up_callback(request, user, **kwargs):
    user_profile = UserProfile()
    user_profile.user = user
    user.save()
    user_profile.save()
