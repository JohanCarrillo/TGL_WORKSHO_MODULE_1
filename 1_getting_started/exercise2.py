def fahrenheit_to_celsius(temperature_in_fahrenheit: float) -> float:
  """Converts Celsius to Fahrenheit

  Args:
      temperature_in_fahrenheit (float): Temperature in Celsius

  Returns:
      float: temperature in Fahrenheit
  """

  return (temperature_in_fahrenheit - 32) / (9/5)

def get_float() -> float:
  """get a float number from the user

  Returns:
      float: number the user enter
  """
  n = ''
  while(type(n) != float):
    try:
      n = float(input("Enter the temperature in Celsius: "))
    except:
      print("Invalid temperature")
    else:
      return n

def main():
  t = get_float()
  print(f"The temperature is: {round(fahrenheit_to_celsius(t), 3)} °C")

if __name__ == "__main__":
  main()