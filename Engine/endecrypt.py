# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from myLog import logg

# ================================================================================#
def confReadValue(confFile,blockName,variableName,*separator):

    temptext = ''

    try:
        config = configparser.ConfigParser()
        config.read(confFile)
    except errno as e:
        print('Something went wrong: ' + e.message, 'error')
        raise

    if not separator:
        temptext = config[blockName][variableName]
    else:
        temptext = config[blockName][variableName].split(separator)

    return temptext or 'Not get back any value.. probably its empty.'