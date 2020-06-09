import codecs

# http://www.data-compression.com/english.html
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def singlechar_xor(input_bytes, byte_candidate):
    output = [input_byte ^ byte_candidate for input_byte in input_bytes]

    return bytearray(output)

def calculate_english_score(bytes):
    score = 0
    for b in bytes:
        score += CHARACTER_FREQ.get(chr(b),0)

    return score


def single_byte_xor_cipher(cipher_text):
    cipher_b16 = codecs.decode(cipher_text, 'hex')

    result = {
        'score' : 0,
        'text'  : "",
        'byte'  : b''}

    for byte_candidate in range(0x00,0xff):
        plaintext = singlechar_xor(cipher_b16, byte_candidate)
        score = calculate_english_score(plaintext)

        if score > result['score']:
            result['score'] = score
            result['text'] = plaintext
            result['byte'] = byte_candidate

    result['text'] = result['text'].decode()
    return result
