# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import errno
import pygame
from gtts import gTTS
from time import sleep
from myLog import logg
from mutagen.mp3 import MP3
from configSetting import confReadValue

class speechResponseClass (object):
    #================================================================================#
    # Variables
    configFile = 'configs/engine.ini'

    # ================================================================================#
    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.directory = confReadValue(self.configFile,'SPRP','directory')
        self.speakTempFile = self.directory + 'temp'+confReadValue(self.configFile,'SPRP','extension')
        self.language = confReadValue(self.configFile,'SPRP','language')

        self.speechWasInitailized = True
        logg('Initalizing the speechResp.', 'info')
        self.folderIsExist(self.directory)
        pygame.init()
        logg('SpeechResponseClass: Self init done.', 'info')

    #================================================================================#
    def folderIsExist(self,path):
        logg('Checking the folders...', 'info')
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                logg('In speechResp '+path+' directory was created!', 'info')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    logg('Something went wrong: '+e.message, 'error')
                    raise
        else:
            logg('In speechResp '+path + ' directory already exist!', 'info')

    #================================================================================#
    def speechResp(self,vcText):

        if not vcText:
            tts = gTTS(text='Please try again.', lang=self.language)
        else:
            tts = gTTS(text=vcText, lang=self.language)

        tts.save(self.speakTempFile)

        pygame.mixer.music.load(self.speakTempFile)
        pygame.mixer.music.play(0)
        logg('Speeching: < '+vcText+' >', 'info')

        audio = MP3(self.speakTempFile)
        logg('Audio leng: '+str(audio.info.length), 'info')

        sleep(audio.info.length)

        #print ('Remove...')
        #os.remove(speakTempFile)
