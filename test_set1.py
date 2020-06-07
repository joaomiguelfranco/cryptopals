import unittest
import  set1

class Test_Set1(unittest.TestCase):
    def test_convert_hex_to_base64_long_string(self):
        input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n'

        result = set1.convert_hex_to_base64(input)

        self.assertEqual(expected_output, result)

    def test_fixed_xor_mine(self):
        hex_input = '1c0111001f010100061a024b53535009181c'
        xor_against = '686974207468652062756c6c277320657965'

        expected_result = '746865206b696420646f6e277420706c6179'

        result = set1.fixed_xor_mine(hex_input, xor_against)

        self.assertEqual(expected_result, result)

    def test_fixed_xor_simpler(self):
        hex_input = '1c0111001f010100061a024b53535009181c'
        xor_against = '686974207468652062756c6c277320657965'

        expected_result = '746865206b696420646f6e277420706c6179'

        result = set1.fixed_xor_simpler(hex_input, xor_against)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
