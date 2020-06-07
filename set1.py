from binascii import b2a_base64
import codecs

def convert_hex_to_base64(input):
    b16 = codecs.decode(input,'hex')
    b64 = codecs.encode(b16, 'base64')
    return b64.decode()


def fixed_xor_mine(hex_input, xor_against):
    b16_1 = codecs.decode(hex_input, 'hex')
    b16_2 = codecs.decode(xor_against, 'hex')

    assert len(b16_1) == len(b16_2)

    result = []
    for byte1, byte2 in zip(b16_1, b16_2):
        result.append(byte1 ^ byte2)

    b16_res = bytearray(result)
    return codecs.encode(b16_res,'hex').decode()

def fixed_xor_simpler(hex1, hex2):
    hex1 = int(hex1, 16)
    hex2 = int(hex2, 16)
    xor = hex1 ^ hex2

    return hex(xor)[2:]