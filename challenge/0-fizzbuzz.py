#!/usr/bin/env python3
import sys

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        if i % 3 and i % 5:
            print(i, end="")
        print(" ", end="")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
    else:
        fizzbuzz(int(sys.argv[1]))
