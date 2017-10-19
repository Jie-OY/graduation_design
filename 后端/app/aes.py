# -*- coding: utf-8 -*-


"""
    AES 对称加密算法 （https://stackoverflow.com/a/39657872/7962085）
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: aes.py
@time: 2017/8/24 23:11 
"""
from Crypto.Cipher import AES  # pip install pycrypto,not crypto
import base64

# Key
tmp1 = "Guz(%&hj7x89H$yuBI0456FtmaT5&fvHUFCy76*h%(HilJ$lhj!y6&(*jkP87jH7"
# Iv
tmp2 = "E4ghj*Ghg7!rNIfb&95GUY86GfghUb#er57HBh(u%g6HJ($jhWk7&!hg4ui%$hjk"
# padding算法
BS = AES.block_size  # aes數據分組長度為128 bit

import base64
from Crypto.Cipher import AES

KEY = 'Guz(%&hj7x89H$yuBI0456FtmaT5&fvH'
IV = "E4ghj*Ghg7!rNIfb"


class AESCipher:
    class InvalidBlockSizeError(Exception):
        """Raised for invalid block sizes"""
        pass

    def __init__(self):
        self.key = KEY
        self.iv = bytes(IV, 'utf-8')

    def __pad(self, text):
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    def encrypt(self, raw):
        raw = self.__pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return (base64.b64encode(cipher.encrypt(raw))).decode()

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.__unpad(cipher.decrypt(enc).decode("utf-8"))


e = AESCipher()
encrypt = e.encrypt
decrypt = e.decrypt


# 測試模塊
if __name__ == '__main__':
    secret_data = "123456"
    enc_str = encrypt(secret_data)
    print('enc_str: ' + enc_str)
    dec_str = decrypt(enc_str)
    print('dec str: ' + dec_str)
