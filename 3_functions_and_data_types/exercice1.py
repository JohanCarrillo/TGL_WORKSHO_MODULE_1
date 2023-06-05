def find_maximum(numbers_list: list) -> float:
  if len(numbers_list) > 0:
    max_num = numbers_list[0]
    for n in numbers_list:
      max_num = n if n > max_num else max_num
    return max_num
  else:
    print("Empty list")
    raise ValueError("Empty list")

def main():
  numbers_list = [-1, 2, -4, -100, -1000, 25, -67, 0]
  try:
    max_num = find_maximum(numbers_list)
  except:
    print("Error")
  else:
    print(f"The biggest number is {max_num}")

if __name__ == "__main__":
  main()