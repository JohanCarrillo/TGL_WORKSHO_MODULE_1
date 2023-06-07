def is_palindrome(word_to_test: str) -> bool:
  """Checks if a given string is a palindrome

  Args:
      word_to_test (str): string to check

  Returns:
      bool: indicates if the given string is a palindrome
  """

  for i in range(len(word_to_test) // 2):
    if(word_to_test[i] != word_to_test[-(i+1)]):
      return False
  return True