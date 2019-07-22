from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    # path('media_tweets/', views.tweet_list, name='media_tweet_list'),

    path('<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('create/', views.tweet_create, name='tweet_create'),
    
]
