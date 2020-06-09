import codecs

def xor_two_lists(l1, l2):
    assert len(l1) == len(l2)

    result = bytearray()
    for byte1, byte2 in zip(l1, l2):
        result.append(byte1 ^ byte2)

    return result

def fixed_xor_mine(hex_input, xor_against):
    b16_1 = codecs.decode(hex_input, 'hex')
    b16_2 = codecs.decode(xor_against, 'hex')

    b16_res = xor_two_lists(b16_1, b16_2)

    return b16_res.hex()

def fixed_xor_simpler(hex1, hex2):
    hex1 = int(hex1, 16)
    hex2 = int(hex2, 16)
    xor = hex1 ^ hex2

    return hex(xor)[2:]