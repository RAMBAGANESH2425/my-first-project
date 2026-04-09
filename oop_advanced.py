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
        print(f"Student Name: {self.name}, Age: {self.__age}")
class Teacher(Person):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def display(self):
        print(f"Teacher Name: {self.name}, Subject: {self.subject}")
s1 = Student("Jahnavi", 20)
t1 = Teacher("Ravi", "Maths")
print("---- Student Details ----")
s1.display()
print("Access Age:", s1.get_age())
s1.set_age(21)
print("Updated Age:", s1.get_age())
print("\n---- Teacher Details ----")
t1.display()
