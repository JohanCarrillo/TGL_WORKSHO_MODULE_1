def fibonacci(n: int) -> list:
  """Generate a list with the n first Fibonacci numbers

  Args:
      n (int): number of Fibonacci numbers to generate

  Returns:
      list: list with the first n Fibonacci numbers
  """

  fibonacci_list = [0]
  for i in range(n):
    if i != 1 and i != 0:
      fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i])
    elif i == 1:
      fibonacci_list.append(1)
    else:
      fibonacci_list.append(1)
  
  return fibonacci_list

def get_int() -> int:
  """get an int number from the user

  Returns:
      int: number the user enter
  """
  n = ''
  while(type(n) != int):
    try:
      n = int(input("Enter an integer number to generate the sequence: "))
    except:
      print("Invalid input")
    else:
      return n

def main():
  n = get_int()
  fibonacci_list = fibonacci(n)
  fibonacci_string = ", ".join([str(i) for i in fibonacci_list])
  print(fibonacci_string)

if __name__ == "__main__":
  main()