from django.contrib import admin
from .models import UserProfile, UserKeyword

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserKeyword)
