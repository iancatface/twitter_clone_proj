from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from .forms import TweetCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.contrib import messages


def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweets/tweet_detail.html', {'tweet': tweet})

def tweet_create(request):
    if request.method == 'POST':
        form = TweetCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.author = request.user
            new_tweet.save()
            messages.success(request, 'ur tweet have been posted!')
            return redirect('tweets:tweet_list')
    else:
        form = TweetCreationForm(data=request.GET)
    return render(request, 'tweets/tweet_create.html', {'form': form})

# class TweetCreateView(CreateView):
#     model = Tweet
#     form_class = TweetCreationForm
#     template_name = 'tweets/tweet_create.html'
#     success_url = reverse_lazy('tweet_list')
    