# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>
"""


This module uses Windows Component Object Model (COM) objects to invoke Windows' native
speech synthesis API (currently SAPI5, Speech Application Programming Interface).

Refs:

* https://docs.microsoft.com/en-us/windows/win32/com/the-component-object-model
* https://en.wikipedia.org/wiki/Microsoft_Speech_API
* https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_application_programming_interfaces_and_frameworks


Prior art, Python TTS packages:
-------------------------------

Python TTS packages

* pyttsx3:
    * https://pypi.org/project/pyttsx3/

* sapitts:
    * https://pypi.org/project/sapitts/
    * https://github.com/DeepHorizons/tts/blob/master/tts/sapi.py

* pytalker
    * https://pypi.org/project/pytalker/

* py-espeak-ng
    * https://pypi.org/project/py-espeak-ng/

* yandex_speech
    * https://pypi.org/project/yandex_speech/

* ttsbroker:
    * https://pypi.org/project/ttsbroker/

* tts-watson
    * https://pypi.org/project/tts-watson/

* gTTS
    * https://pypi.org/project/gTTS/

"""

# If `win32com.client` is not available, we could also use `comtypes` (pure python/ctypes)
import win32com.client

# speech = win32com.client.Dispatch('System.Speech.Synthesis.SpeechSynthesizer')  # Doesn't work
spvoice = win32com.client.Dispatch('SAPI.SPVoice')


def reinitialize_voice():
    global spvoice
    # del spvoice
    spvoice = win32com.client.Dispatch('SAPI.SPVoice')
    return spvoice


def speak(sentence):
    return spvoice.Speak(sentence.encode('utf-8'), 19)  # returns immediately.


def pause():
    return spvoice.Pause()  # returns immediately.


def resume():
    return spvoice.Resume()  # returns immediately.


def skip(num_skip=1):
    return spvoice.Skip("Sentence", num_skip)  # returns immediately.


def skip_all():
    return skip(num_skip=1000)


def speak_and_wait_until_done(sentence):
    return spvoice.WaitUntilDone(sentence.encode('utf-8'), 19)  # blocks until done.
