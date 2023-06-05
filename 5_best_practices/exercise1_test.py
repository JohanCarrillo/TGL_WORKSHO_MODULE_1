import unittest

from exercise1 import is_palindrome


class TestIsPalindrome(unittest.TestCase):
  def test_is_palindrome_odd_word(self):
    test_case = "kayak"
    self.assertTrue(is_palindrome(test_case))

  def test_is_palindrome_even_word(self):
    test_case = "peep"
    self.assertTrue(is_palindrome(test_case))

  def test_is_not_palindrome_odd_word(self):
    test_case = "cat"
    self.assertFalse(is_palindrome(test_case))

  def test_is_not_palindrome_even_word(self):
    test_case = "cats"
    self.assertFalse(is_palindrome(test_case))

if __name__ == '__main__':
    unittest.main()