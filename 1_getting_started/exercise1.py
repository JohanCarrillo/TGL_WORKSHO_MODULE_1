def sum(n: float, m: float) -> float:
  """Takes two numbers and returns their sum

  Args:
      n (float): first number to sum
      m (float): second number to sum

  Returns:
      float: sum of the arguments
  """

  return n + m

def get_float() -> float:
  """get a float number from the user

  Returns:
      float: number the user enter
  """
  n = ''
  while(type(n) != float):
    try:
      n = float(input("Enter a number: "))
    except:
      print("Invalid input")
    else:
      return n

def main():
  num_1 = get_float()
  num_2 = get_float()
  print(f'{num_1} + {num_2} = {sum(num_1, num_2)}')

if __name__ == "__main__":
  main()