import math

def square_num(n):
    return n * n

def find_log(n):
    try:
        return math.log(n)
    except ValueError:
        return "Invalid input for log"