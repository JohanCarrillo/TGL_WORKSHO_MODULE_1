def get_str() -> str:
  """get a string from the user

  Returns:
      str: string the user enters
  """
  s = ""
  try:
    s = input("Enter a string to reverse: ")
  except:
    print("Invalid input")
  else:
    return s

def reverse_string(s: str, i = 0, s_list = []) -> str:
  """reverses a tring recursively

  Args:
      s (str): string to reverse
      i (int, optional): counter for recursivity. Defaults to 0.
      s_list (list, optional): accumulator for recursivity. Defaults to [].

  Returns:
      str: _description_
  """
  step = len(s) - i

  if step > 0:
    i+=1
    s_list.append(s[step - 1])
    return reverse_string(s, i, s_list)
  else:
    reversed_s = "".join(s_list)
    return reversed_s

def main():
  string_to_reverse = get_str()
  if string_to_reverse:
    reversed_s = reverse_string(string_to_reverse)
    print(reversed_s)
  else:
    print("")

if __name__ == "__main__":
  main()