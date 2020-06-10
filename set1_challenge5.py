import codecs

class Repeating_Cipher:
    def __init__(self, cipher):
        self.cipher = bytearray(cipher, 'utf8')
        self.count = 0

    def get_cipher_byte(self):
        index = self.count % len(self.cipher)
        output = self.cipher[index]
        self.count += 1

        return output


def cipher_repeating_xor(text_to_cipher, cipher):
    bytes_to_cipher = bytearray(text_to_cipher, 'utf8')
    cipher = Repeating_Cipher(cipher)

    xor_func = lambda x : x ^ cipher.get_cipher_byte()

    ciphered_list = list(map(xor_func, bytes_to_cipher))
    ciphered_bytes = bytearray(ciphered_list)

    ciphered_hex = codecs.encode(ciphered_bytes, 'hex')

    return ciphered_hex.decode()

