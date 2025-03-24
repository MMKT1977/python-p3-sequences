#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    if length >= 1:
        fibonacci.append(0)
    if length >=2:
        fibonacci.append(1)
    for i in range (2,length):
        next_number = fibonacci[-1]+ fibonacci[-2]
        fibonacci.append(next_number)
    print(fibonacci)
print_fibonacci(11)

    