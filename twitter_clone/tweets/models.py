from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


class Tweet(models.Model):
    author = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    body = models.CharField(max_length=280, blank=True, null=True)
    image = models.ImageField(upload_to='img/request.user.username/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tweets_like')
    users_retweet = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tweets_retweet')

    def __str__(self):
        return self.id

    # def get_absolute_url(self):
    #     return reverse("tweet_detail", kwargs={"pk": self.pk})
    
