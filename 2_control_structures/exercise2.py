def check_prime(n: int) -> bool:
  """Checks if the given number is a prime

	Args:
			n (int): number to check

	Returns:
			bool: True or False depending if it is prime
  """

  if n % 2 == 0:
    return False
  elif n == 2 or n == 1:
    return True
  else:
    for i in range(3, n, 2):
      if n % i == 0:
        return False
    return True

def get_int() -> int:
  """get an int number from the user

  Returns:
      int: number the user enter
  """
  n = ''
  while(type(n) != int):
    try:
      n = int(input("Enter an integer number: "))
      if n <= 0:
        raise Exception("Invalid input")
    except:
      print("Invalid input")
    else:
      return n

def main():
  n = get_int()
  print(f"Checing if {n} is a prime")
  print(str(check_prime(n)))

if __name__ == "__main__":
  main()