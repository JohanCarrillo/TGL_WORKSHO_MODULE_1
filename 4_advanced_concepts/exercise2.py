def count_words(text: str) -> dict:
  """count each word in the input and returns the total count of each

  Args:
      text (str): string to count

  Returns:
      dict: dictionary with each word count
  """

  str_array = text.split()
  registry = {}
  
  for word in str_array:
    if word in registry:
      registry[word] += 1
    else:
      registry[word] = 1

  return registry

def read_file(file_name: str) -> str:
  """read a file and returns its content as string

  Args:
      file_name (str): the name or path of the file

  Returns:
      str: the content of the file
  """

  try:
    f = open(file_name, 'r')
    content = f.read()
    f.close()
  except:
    print("Error opening file")
    content = ""
  finally:
    return content

def main():
  file_name = input("Enter file name or path: ")
  # file_name = "zen_of_python.txt"
  file_text = read_file(file_name)

  if file_text == "":
    return 0

  words_dict = count_words(file_text)

  for word in words_dict:
    print(f"{word}: {words_dict[word]}")

if __name__ == "__main__":
  main()
