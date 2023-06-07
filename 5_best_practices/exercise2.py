import time
import random

def timer(func: function):
  """decorator that logs total execution time of given function

  Args:
      func (function): function to decorate
  """
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"runtime for {func.__name__}: {end - start} seconds")
    return result
  return wrapper

@timer
def unoptimized_sorter(numbers_list: list) -> list:
  """sort a list of given numbers. Mutates the original array. O(n**2)

  Args:
      numbers_list (list): list of numbers to sort

  Raises:
      Exception: Invalid value found in list
      Exception: list is empty

  Returns:
      list: original list but sorted
  """

  length = len(numbers_list)
  if length > 0:
    for i in range(length):
        for j in range(0, length - i - 1):
          try:
            if numbers_list[j] > numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
          except:
            raise Exception("Invalid value found")
          else:
            continue
    return numbers_list
  else:
    raise Exception("Empty list")

def main():
  random_array = [random.random() * 100 for _ in range(10000)]

  try:
    sorted_list = unoptimized_sorter(random_array)
  except:
    print("Error found")
  else:
    print(f"sorted list: {sorted_list}")

if __name__ == "__main__":
  main()