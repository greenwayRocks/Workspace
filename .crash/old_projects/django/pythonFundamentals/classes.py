# Class of objects

# Create class


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Init user object
brad = User('Brad Traversy', 'email@gmail.com', 37)

# Edit
brad.age = 38


# Call method
print(brad.greeting())

brad.has_birthday()


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance


# Object Customer
john = Customer('John Doe', 'john@email', 37)

print(john.name)

# john.set_balance(200)
john.balance = 200

print(john.balance)
