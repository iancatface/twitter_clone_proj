# Generated by Django 2.2.3 on 2019-07-21 18:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='tweets_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='users_retweet',
            field=models.ManyToManyField(blank=True, related_name='tweets_retweet', to=settings.AUTH_USER_MODEL),
        ),
    ]
