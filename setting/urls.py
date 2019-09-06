from django.urls import path, include
from django.contrib import admin
from .views import views,api

urlpatterns = [
    path('setting/', views.setting, name='setting_setting'),
    path('POST/restart_service/', api.post_restart_service, name='settings_post_restart_service')

]
