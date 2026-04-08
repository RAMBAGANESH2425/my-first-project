from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def display(self):
        pass
class Student(Person):  
    def __init__(self, name, age):
        self.name = name         
        self.__age = age          
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.__age)
s1 = Student("Jahnavi", 20)
print("---- Student Details ----")
s1.display()
print("Accessing age using getter:", s1.get_age())
s1.set_age(21)
print("Updated Age:", s1.get_age())