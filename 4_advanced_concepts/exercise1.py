class BankAccount:
  __current_balance: float

  def __init__(self, initial_amout: int):
    self.__current_balance = initial_amout
    
  def check_balance(self):
    return self.__current_balance

  def deposit(self, ammount: float):
    if ammount >= 0:
      self.__current_balance += ammount
  
  def withdraw(self, ammout: float):
    if ammout >= 0:
      self.__current_balance -= ammout