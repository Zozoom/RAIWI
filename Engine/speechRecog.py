# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import speech_recognition as sr
from myLog import logg

class speechRecogClass (object):
    # ================================================================================#
    # Variables
    rec = ''
    recWasInitailized = ''

    # ================================================================================#
    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.rec = sr.Recognizer()
        self.recWasInitailized = False
        logg('SpeechRecogClass: Self init done.', 'info')

    # ================================================================================#
    def speechRec(self):

        recognisedtext = ''

        with sr.Microphone() as source:
            audio = self.rec.listen(source)

        try:
            recognisedtext = str(self.rec.recognize_google(audio))
            logg("You said: " + recognisedtext, 'info')

        except sr.UnknownValueError:
            message = "Could not understanded audio."
            logg(message, 'error')

        except sr.RequestError as e:
            message = "Could not request results; {0}".format(e)
            logg(message, 'error')

        return recognisedtext or ""