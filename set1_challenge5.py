import codecs

def build_cipher_list(cipher, text_len):
    if len(cipher) > text_len: return cipher[0:text_len]

    cipher_list = cipher * (text_len // len(cipher))

    cipher_list += cipher[0:text_len - len(cipher_list)]

    return cipher_list

def get_bytes_to_cipher(cipher, text_len):
    return bytearray(
            build_cipher_list(cipher,text_len),
            'utf8')


def cipher_repeating_xor(text_to_cipher, cipher):
    bytes_to_cipher = bytearray(text_to_cipher, 'utf8')
    cipher = get_bytes_to_cipher(cipher, len(text_to_cipher))

    xor_func = lambda x,y : x ^ y

    ciphered_list = (list(map(xor_func, bytes_to_cipher, cipher)))
    ciphered_bytes = bytearray(ciphered_list)

    ciphered_hex = codecs.encode(ciphered_bytes, 'hex')

    return ciphered_hex.decode()

