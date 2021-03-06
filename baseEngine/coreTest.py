# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from myLog import logg
import speechRecog
import speechResponse

# ================================================================================#
def main():

    # Starting section
    logg('Start the SpeechRec python...', 'info')
    speechRecognizer = speechRecog.speechRecogClass()

    logg('Start the SpeechResp python...', 'info')
    speechResponizer = speechResponse.speechResponseClass()

    print 'Waiting...'
    text = speechRecognizer.speechRec()
    print 'Sepaking...'
    speechResponizer.speechResp(text)

# ================================================================================#
if __name__ == "__main__":
    main()