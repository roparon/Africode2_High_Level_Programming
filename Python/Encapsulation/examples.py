class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner  # Public attribute
        self._balance = initial_balance  # Protected attribute
        self.__pin = "1234"  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposited amount must be positive and greater than 0.")
            return False

    def withdraw(self, amount):
        if 0 <= amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
            return True
        else:
            print("Withdrawal amount must be positive and less than or equal to current balance.")
            return False

    def get_balance(self):
        return self._balance

    # Getter for PIN
    def get_pin(self):
        return self.__pin

    # Setter for PIN
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():  # Validate the new PIN
            self.__pin = new_pin
            print("PIN successfully changed.")
        else:
            print("Invalid PIN. PIN must be a 4-digit number.")

# Example usage
account = BankAccount("Ben", 10000)

# Accessing the PIN using the getter
print("Current PIN:", account.get_pin())

# Changing the PIN using the setter
account.set_pin("5678")
print("New PIN:", account.get_pin())