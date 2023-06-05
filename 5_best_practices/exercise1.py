def is_palindrome(word_to_test: str):
  for i in range(len(word_to_test) // 2):
    if(word_to_test[i] != word_to_test[-(i+1)]):
      return False
  return True