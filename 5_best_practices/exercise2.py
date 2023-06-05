import time
import random

def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"runtime for {func.__name__}: {end - start} seconds")
    return result
  return wrapper

@timer
def unoptimized_sorter(numbers_list: list) -> list:
  if len(numbers_list) > 0:
    max = numbers_list[0]
    for n in numbers_list:
      max = n if n > max else max
    print(max)
    return max
  else:
    raise Exception("Empty list")

def main():
  random_array = [random.random() * 100 for _ in range(100000000)]
  try:
    max = unoptimized_sorter(random_array)
  except:
    print("Empty list")
  else:
    print(f"greatest number: {max}")

if __name__ == "__main__":
  main()