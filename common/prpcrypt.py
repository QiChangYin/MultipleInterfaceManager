#!/usr/bin/python
# -*- coding: utf-8 -*-

from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex
from MultipleInterfaceManager.settings import PRPCRYPT_KAY_SALT

AES_LENGTH = 16
key = PRPCRYPT_KAY_SALT
mode = AES.MODE_ECB


# 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
# 加密内容需要长达16位字符，所以进行空格拼接
def pad(text):
    while len(text) % AES_LENGTH != 0:
        text += ' '
    return text

# 加密密钥需要长达16位字符，所以进行空格拼接
def pad_key(key):
    while len(key) % AES_LENGTH != 0:
        key += ' '
    return key

def data_encrypt(text):

    # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
    # 加密的字符需要转换为bytes
    # print(self.pad(text))
    cryptor = AES.new(pad_key(key).encode(), mode)
    ciphertext = cryptor.encrypt(pad(text).encode())
    # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串
    return b2a_hex(ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉

def data_decrypt(text):
    cryptor = AES.new(pad_key(key).encode(), mode)
    plain_text = cryptor.decrypt(a2b_hex()).decode()
    return plain_text.rstrip(' ')

