import unittest
from set1_challenge1 import convert_hex_to_base64

class Test_Set1(unittest.TestCase):
    def test_convert_hex_to_base64_long_string(self):
        input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n'

        result = convert_hex_to_base64(input)

        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    unittest.main()
