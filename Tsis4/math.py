#1
import math
d = int(input("input degree: "))
print(f"{d} Degrees is equal to Radians : ", end ="")
print(math.radians(d))

#2
h = int(input("Height: "))
b1 = int(input("Base 1: "))
b2 = int(input("Base 2: "))

print(f"Area of trapezoid is: {((b1+b2)/2) * h}")


#3
from math import tan, pi

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
a = n * (s ** 2) // (4 * tan(pi / n))
print("Area of polygon is: ", a)



#4
L = float(input("Length of base: "))

H = float(input("Height of parallelogram: "))

print(f"Expected Output: {L * H}")


