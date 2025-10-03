class BaseClass:
    def __init__(self):
        self._protected_variable = "I am protected"
        self.__private_variable = "I am private"

    def _protected_method(self):
        return "This is a protected method"

    def __private_method(self):
        return "This is a private method"

    def public_method(self):
        print(self.__private_method())  # Accessing private method within the class
        print(self.__private_variable)  # Accessing private variable within the class
        return "This is a public method"

base = BaseClass()
print(base._protected_variable)  # Accessing protected variable (not recommended)
print(base._protected_method())   # Accessing protected method (not recommended)

# print(base.__private_variable)  # This will raise an AttributeError
# print(base.__private_method())   # This will raise an AttributeError

print(base.public_method())  # Accessing public method
