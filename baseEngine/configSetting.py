# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import errno
import os
import configparser

# ================================================================================#
def confReadValue(confFile,blockName,variableName,*separator):

    temptext = ''

    # print confFile +' | '+ blockName +' | '+ variableName
    # print os.getcwd()+'/'+confFile

    try:
        config = configparser.ConfigParser()
        config.read(confFile)

    except errno as e:
        print('Something went wrong: ' + e.message, 'error')
        raise

    if not separator:
        temptext = config[blockName][variableName]
    elif separator:
        temptext = config[blockName][variableName].split(separator)


    return temptext or 'Not get back any value.. probably its empty.'