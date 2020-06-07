from binascii import b2a_base64
import codecs

def convert_hex_to_base64(input):
    b16 = codecs.decode(input,'hex')
    b64 = codecs.encode(b16, 'base64')
    return b64.decode()
