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


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        else:
            return f"'{self.title}' is currently not available."

    def return_book(self):
        if not self.available:
            self.available = True
            return f"You have returned '{self.title}'."
        else:
            return f"'{self.title}' was not borrowed."

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []


    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            return f"{self.name} has borrowed '{book.title}'."
        else:
            return f"'{book.title}' is not available."

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"{self.name} has returned '{book.title}'."
        else:
            return f"{self.name} did not borrow '{book.title}'."

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added '{book.title}' to the library."

    def register_user(self, user):
        self.users.append(user)
        return f"Registered user '{user.name}'."

    def list_available_books(self):
        available_books = [book.title for book in self.books if book.available]
        return available_books if available_books else "No books available."

print("Library System Simulation")

book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
library = Library()
print(library.add_book(book1))
print(library.add_book(book2))
user1 = User("Danniel", 1)
print(library.register_user(user1))
print(library.list_available_books())
print(user1.borrow_book(book1))
print(library.list_available_books())
print(user1.return_book(book1))
print(library.list_available_books())
