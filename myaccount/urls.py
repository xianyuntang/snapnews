from django.urls import path, include
from myaccount.views import views, api


app_name = 'myaccount'
urlpatterns = [
    path('profile/update/', views.profile_update, name='myaccount_profile_update'),
    path('keyword/', views.keyword, name='myaccount_keyword'),
    path('POST/add_keyword_group', api.add_keyword_group, name='myaccount_add_keyword_group'),
    path('POST/mod_keyword_group', api.mod_keyword_group, name='myaccount_mod_keyword_group'),
    path('POST/del_keyword_group', api.del_keyword_group, name='myaccount_del_keyword_group'),
    path('POST/del_keyword', api.del_keyword, name='myaccount_del_keyword'),
    path('POST/add_keyword', api.add_keyword, name='myaccount_add_keyword'),

]
