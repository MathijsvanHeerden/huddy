from django.shortcuts import render
from playsound import playsound
from text_to_speech.TextToSpeech import TextToSpeech
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
