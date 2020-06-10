import unittest
import os

from set1_challenge1 import convert_hex_to_base64
from set1_challenge2 import \
    fixed_xor_mine,\
    fixed_xor_simpler,\
    xor_two_lists
from set1_challenge3 import \
    single_byte_xor_cipher, \
    calculate_english_score

from set1_challenge4 import detect_single_char_xor

class Test_Set1(unittest.TestCase):
    def test_convert_hex_to_base64_long_string(self):
        input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n'

        result = convert_hex_to_base64(input)

        self.assertEqual(expected_output, result)

    def test_fixed_xor_mine(self):
        hex_input = '1c0111001f010100061a024b53535009181c'
        xor_against = '686974207468652062756c6c277320657965'

        expected_result = '746865206b696420646f6e277420706c6179'

        result = fixed_xor_mine(hex_input, xor_against)

        self.assertEqual(expected_result, result)

    def test_xor_two_lists_check_result(self):
        l1 = '1100'
        l2 = '1010'
        expected_result = '0110'

        result = fixed_xor_mine(l1, l2)

        self.assertEqual(expected_result,
                         result)

    def test_xor_two_lists_check_assert(self):
        l1 = []
        l2 = [1,2,3]

        self.assertRaises(AssertionError,
                          xor_two_lists,
                          l1,
                          l2)

    def test_fixed_xor_simpler(self):
        hex_input = '1c0111001f010100061a024b53535009181c'
        xor_against = '686974207468652062756c6c277320657965'

        expected_result = '746865206b696420646f6e277420706c6179'

        result = fixed_xor_simpler(hex_input, xor_against)

        self.assertEqual(expected_result, result)

    def test_score_calculation_non_text(self):
        input_bytes = bytearray(b'\x1c004618\x7f\x12\x1cx,\x7f364:\x7f>\x7f/0*1;\x7f09\x7f=><01')
        score_result = calculate_english_score(input_bytes)
        self.assertLess(score_result, 0.01)

    def test_score_calculation_english_text(self):
        input_bytes = bytearray(b"english text")
        score_result = calculate_english_score(input_bytes)
        self.assertGreater(score_result, 0.80)

    def test_single_byte_xor_cipher(self):
        cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

        expected_byte = 88
        expected_text = "Cooking MC\'s like a pound of bacon"

        result = single_byte_xor_cipher(cipher)

        self.assertEqual(expected_byte,
                         result.byte)
        self.assertEqual(expected_text,
                         result.text)

    def test_detect_singlechar_xor_challenge4_file(self):
        filepath = os.path.join(os.getcwd(),'data','challenge4.txt')
        expected_byte = 53
        expected_text = "Now that the party is jumping\n"

        result = detect_single_char_xor(filepath)

        self.assertEqual(expected_text,
                         result.text)

        self.assertEqual(expected_byte,
                         result.byte)


    def test_detect_singlechar_xor_file_nok(self):
        filepath = os.path.join(os.getcwd(),'some_dir_that_doesnt_exist','filename_nok')
        self.assertRaises(AssertionError,
                          detect_single_char_xor,
                          filepath)

if __name__ == '__main__':
    unittest.main()
