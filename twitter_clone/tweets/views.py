from django.shortcuts import render, get_object_or_404
from .models import Tweet
from .forms import TweetCreationForm


def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweets/tweet_detail.html', {'tweet': tweet})

