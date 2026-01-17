# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Привіт, мене звати {self.name}, мені {self.age} років.")




# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)




# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def get_info(self):
#         return f"{self.brand} {self.model}, {self.year} року"




# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)



# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Недостатньо коштів")
#     def get_balance(self):
#         return self.__balance



# class Book:
#     count = 0
#     def __init__(self, title):
#         self.title = title
#         Book.count += 1





# class Animal:
#     def make_sound(self):
#         print("Тварина видає звук")
# class Dog(Animal):
#     def make_sound(self):
#         print("Гав")
# class Cat(Animal):
#     def make_sound(self):
#         print("Мяу")
# class Employee:
#     def __init__(self, salary):
#         self.salary = salary

#     def get_salary(self):
#         return self.salary
    
# class Manager(Employee):
#     def __init__(self, salary, bonus):
#         super().__init__(salary)
#         self.bonus = bonus

#     def get_salary(self):
#         return self.salary + self.bonus




# class Cow(Animal):
#     def make_sound(self):
#         print("Му")
# animals = [Dog(), Cat(), Cow()]
# for animal in animals:
#     animal.make_sound()



from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

