def say_hi ():
    print("Hi")

say_hi()

def print_square_of_7():
    return 7 * 7

print(print_square_of_7())

from random import random

def coin_flip():
    if random() > 0.5:
        return "heads"
    else:
        return "tails"

print(coin_flip())

def generate_evens():
    return [num for num in range(1, 50) if num % 2 == 0]