class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self): # method to greet the person
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Danniel", 35)
print(person1.greet())

person2 = Person("Alice", 30)
print(person2.greet())


class Bank:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            return f"Deposited {amount}. New balance is {self.balance}."
        else:
            return "Account is inactive. Cannot deposit."

    def withdraw(self, amount):
        if self.is_active:
            if amount > self.balance:
                return "Insufficient funds."
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        else:
            return "Account is inactive. Cannot withdraw."

    def deactivate_account(self):
        self.is_active = False
        return "Account has been deactivated."

    def activate_account(self):
        self.is_active = True
        return "Account has been activated."

account1 = Bank("Danniel", 1000)
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.deactivate_account())
print(account1.deposit(100))  # Should not allow deposit
print(account1.activate_account())
print(account1.withdraw(300))
