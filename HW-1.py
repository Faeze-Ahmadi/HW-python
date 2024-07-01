# HW1
import math
def triangle_properties(a, b, c):
    P = a + b + c
    C = P / 2
    A = math.sqrt(C * (C - a) * (C - b) * (C - c))
    return P, A

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

perimeter, area = triangle_properties(a, b, c)
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")