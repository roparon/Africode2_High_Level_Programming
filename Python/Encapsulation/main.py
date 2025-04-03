class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner #Public attribute
        self._balance = initial_balance #protected attribute
        self.__pin = "1234" #private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposited amount must be positive and greater than 0.")
            return False

    def withdraw(self, amount):
        if 0 <= amount <= self._balance: #(if amount > 0 and amount <= self._balance:)

            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
            return True
        else:
            print("Withdrawal amount must be positive and less than or equal to current balance.")
            return False
        
    def get_balance(self):
        return self._balance
    
    def veryfy_pin(self, attempted_pin):
        return self.__pin == attempted_pin
    
    def change_pin(self, new_pin):
        self.__pin = new_pin
    
account = BankAccount ("Ben", 10000)
# account.owner = "Ronoh"
# print(account.owner) #Public attribute
# account._balance = 2000 #accessing protected attribute directly (not recommended)
# print(account._balance) #Protected attribute (accessible within the class)

# print(account._BankAccount__pin)  # Accessing the private attribute using name mangling

# account.change_pin("5678")
print(account.veryfy_pin("1234")) #
account.change_pin("5678")
