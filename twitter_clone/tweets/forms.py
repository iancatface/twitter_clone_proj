from django import forms
from .models import Tweet

class TweetCreationForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('body', 'image')

    def save(self):
        if not self.body and not self.image:
            raise forms.ValidationError('tweet can not be empty :(')
