from django.urls import path, include
from myaccount.views import views, api

app_name = 'myaccount'
urlpatterns = [
    path('profile/update/', views.profile, name='myaccount_profile'),
    path('keyword/', views.keyword, name='myaccount_keyword'),
    path('profile/update_line_api_key/', views.update_line_api_key, name='myaccount_update_line_api_key')
]
