class BankAccount:
  __current_balance: float

  def __init__(self, initial_amout: float):
    self.__current_balance = initial_amout
    
  def check_balance(self) -> float:
    """returns current balance in the account

    Returns:
        float: _description_
    """
    return self.__current_balance

  def deposit(self, ammount: float):
    """add money to the account

    Args:
        ammount (float): ammount to add to the account
    """
    if ammount >= 0:
      self.__current_balance += ammount
  
  def withdraw(self, ammout: float):
    """substract money from the account

    Args:
        ammout (float): ammount to substract from the account
    """
    if ammout >= 0:
      self.__current_balance -= ammout