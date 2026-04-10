import re
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration
print("Iterator Output:")
counter = CountUp(5)
for num in counter:
    print(num)
def generate_numbers(n):
    for i in range(1, n+1):
        yield i
print("\nGenerator Output:")
for num in generate_numbers(5):
    print(num)
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")

print("\nDecorator Output:")
say_hello()
def outer(msg):
    def inner():
        print("Message:", msg)
    return inner
closure_func = outer("Hello Closure")
print("\nClosure Output:")
closure_func()
text = "My email is test123@gmail.com"
pattern = r'\w+@\w+\.\w+'
result = re.findall(pattern, text)
print("\nRegex Output:")
print(result)