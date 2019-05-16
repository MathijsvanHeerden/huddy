from django import forms
from duddy import models


class RepeatedMessageForm(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = models.RepeatedMessage
        exclude = ['messageFilename']
