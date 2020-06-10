import os
import codecs

from set1_challenge3 import \
    single_byte_xor_cipher, \
    Result

def check_if_file_is_ok(filepath):
    assert os.path.isfile(filepath)

def get_lines(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f.readlines()]

def detect_single_char_xor(ciphered_file):
    check_if_file_is_ok(ciphered_file)

    best_result = Result()
    for ciphered_line in get_lines(ciphered_file):

        result = single_byte_xor_cipher(ciphered_line)

        if result.score > best_result.score:
            best_result = result

    return best_result
