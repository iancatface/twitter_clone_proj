from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

# current_user = get_user_model()
def user_directory_path(instance, filename):
    return 'user_{}/{}'.format(instance.author.id, filename)

class Tweet(models.Model):
    author = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    body = models.CharField(max_length=280, blank=True)
    #DO NOT use null=True on Text and Charfield
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tweets_like', blank=True)
    users_retweet = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tweets_retweet', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}'.format(str(self.id))

    def get_absolute_url(self):
        return reverse('tweets:tweet_detail', args=[self.id])

    def save(self, *args, **kwargs):
        if not self.body and not self.image:
            raise ValidationError('tweet can not be empty :(')
        super().save(*args, **kwargs)
    
    