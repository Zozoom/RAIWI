# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from baseEngine.myLog import logg
from baseEngine.speechRecog import speechRecogClass
from baseEngine.speechResponse import speechResponseClass

# ================================================================================#
def main():

    # Starting section
    logg('Start the SpeechRec python...', 'INFO')
    speechRecognizer = speechRecogClass()

    logg('Start the SpeechResp python...', 'INFO')
    speechResponizer = speechResponseClass()

    print 'Waiting...'
    text = speechRecognizer.speechRec()
    print 'Sepaking...'
    speechResponizer.speechResp(text)

# ================================================================================#
if __name__ == "__main__":
    main()