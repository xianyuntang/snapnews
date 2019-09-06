from django.urls import path
from snapnews.views import views, api

app_name = 'snapnews'
urlpatterns = [
    path('index/', views.index, name='snapnews_index'),
    path('search/', views.search, name='snapnews_search'),
    path('GET/generate_word_cloud/', api.get_generate_word_cloud, name='snapnews_get_generate_word_cloud'),
    path('GET/generate_word_cloud_today_only/', api.get_generate_word_cloud_today_only, name='snapnews_get_generate_word_cloud_today_only'),
    # path('GET/breaking_news/', api.get_breaking_news, name='snapnews_get_breaking_news'),
    path('GET/load_snapshot/', api.load_snapshot, name='snapnews_get_load_snapshot'),
    path('GET/load_single_snapshot/', api.load_single_snapshot, name='snapnews_get_load_single_snapshot'),

]
