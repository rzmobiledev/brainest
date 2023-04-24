"""
Create a Dog class with the following attributes: name, breed, and age. The class should also have the following methods: bark() and info().
"""


# class Dog:

#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age

#     def bark(self):
#         print("{} is barking".format(self.name))

#     def info(self):
#         print("Dog name is: {}, age: {}, breed: {}".format(self.name, self.age, self.breed))


# dog = Dog("Gukguk", "afternoon", 5)

# dog.bark()
# dog.info()


"""
Create a BankAccount class with the following attributes: balance and account_number.
The class should also have the following methods: deposit(amount), withdraw(amount), and info().
"""


# class BankAccount:

#     def __init__(self, balance, account_number):
#         self.balance = balance
#         self.account_number = account_number

#     def deposit(self, amount=0):
#         self.balance = self.balance + amount
#         self.deposit = amount

#     def withdraw(self, amount=0):
#         self.amount = self.balance - amount
#         self.withdraw = amount
    
#     def info(self):
#         print("Your Account info:")
#         print("-------------------")
#         print("Account Number: {}".format(self.account_number))
#         print("Deposit: {}".format(self.deposit))
#         print("Withdraw: {}".format(self.withdraw))
#         print("Balance: {}".format(self.balance))


# bank = BankAccount(500, 7896541)
# bank.deposit(50)
# bank.withdraw(20)
# bank.info()


"""
Create a Vehicle class with the following attributes: 
make, model, and year. The class should also have the following methods: start(), stop(), and info().

Create a Car class that inherits from the Vehicle class. 
The Car class should have an additional attribute: num_doors. 
The class should also have the following method: lock_doors().
"""


# class Vehicle:

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start():
#         print("The car is starting")

#     def stop():
#         print("The car is stoping")

    

# class Car(Vehicle):

#     def __init__(self, num_doors):
#         Vehicle.__init__(self, num_doors)
#         self.num_doors = num_doors

"""
1.Write a lambda function that takes two lists of integers and returns a new list with the maximum value for each index of the two lists.
For example, given [1, 3, 5] and [2, 4, 6], the function should return [2, 4, 6].
"""

# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# result = list(map(lambda x, y: max(x, y), list1, list2))
# print(result)

"""
2. Write a lambda function that takes a string of words separated by spaces,
and returns a new string with the words in reverse order. For example,
given the string "the quick brown fox", the function should return "fox brown quick the".
"""
# s = "the quick brown fox"
# result = " ".join(reversed(s.split()))
# print(result)

from collections import Counter

all_nums = (10, 20, 10, 30, 40, 40, 30, 20, 5, 6)

find_unique = tuple(x for x, y in Counter(all_nums).items() if y > 1)
print(find_unique)