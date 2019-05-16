from django.shortcuts import render
from playsound import playsound
from text_to_speech.TextToSpeech import TextToSpeech
from duddy import forms
from duddy import models
# Create your views here.


def index(request):
    context = {}
    # playsound('sounds/SampleAudio.mp3')
    app = TextToSpeech()
    app.get_token()
    tts = request.POST.get('tts')
    if tts:
        filename = app.save_audio(tts)
        playsound(filename)

    # app.save_audio()
    return render(request, 'index.html', context)


def repeat(request):
    message = ""
    if request.method == "POST":
        form = forms.RepeatedMessageForm(request.POST)
        if form.is_valid():
            form.save()
            app = TextToSpeech()
            app.get_token()
            app.save_audio(form.cleaned_data['messageText'], repeated=True)
        else:
            message = "Opgeslagen!"
    form = forms.RepeatedMessageForm()
    context = {
        'form': form,
        'message': message if message else None
    }
    return render(request, 'repeat.html', context)


def play(request, sound):
    sounds = models.RepeatedMessage.objects.all()
    context = {
        'sounds': sounds
    }
    app = TextToSpeech()
    app.get_token()
    pass
