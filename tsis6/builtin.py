#1 Write a Python program with builtin function to multiply all the numbers in a list
l = [1, 2, 3, 4, 5]
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply(l))


#2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
s = "AbCd"
low = len([x for x in s if x.islower()])
upp = len([x for x in s if x.isupper()])
print(low, upp)


#3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.

a = "ffgff"


def isPalin(str):
    str = ''.join(x for x in str if x.isalnum()).lower()

    return str == str[::-1]


if isPalin(a):
    print("true")
else:
    print("false")


#4 Write a Python program that invoke square root function after specific milliseconds.
import time
import math
n = int(input())
m = int(input())
time.sleep(m/1000)
print(math.sqrt(n))


#5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
t = (True, True, True)
print(all(t))

