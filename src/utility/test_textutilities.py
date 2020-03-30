import unittest

from src.utility import textutilities


class TestTextUtilities(unittest.TestCase):
    # Test textutilities

    def test_random_string_fixed_size(self):
        result = textutilities.random_string()
        len_result = result.__len__()
        self.assertEqual(len_result, 10)

    def test_random_string_dynamic_size(self):
        result = textutilities.random_string(15)
        len_result = result.__len__()
        self.assertEqual(len_result, 15)

    def test_random_digit_fixed_size(self):
        result = textutilities.random_digit()
        len_result = result.__len__()
        self.assertEqual(len_result, 10)

    def test_random_digit_dynamic_size(self):
        result = textutilities.random_digit(15)
        len_result = result.__len__()
        self.assertEqual(len_result, 15)


if __name__ == '__main__':
    unittest.main()
