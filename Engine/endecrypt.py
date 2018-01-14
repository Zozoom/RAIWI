# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import base64
from Crypto import Random
from Crypto.Cipher import AES
import string
import random

# ================================================================================#
BS = 32
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

# ================================================================================#
class AESCipher:
    # ================================================================================#
    def __init__( self ):
        self.key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(BS))

    # ================================================================================#
    def idgenerator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # ================================================================================#
    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    # ================================================================================#
    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


chiper = AESCipher()
encrypted = chiper.encrypt('thisisthesecretemail@email.com')
decrypted = chiper.decrypt(encrypted)
print 'Key: ' + chiper.key
print 'En: '+encrypted
print 'De: '+decrypted