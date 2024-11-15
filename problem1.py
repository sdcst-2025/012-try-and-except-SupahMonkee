#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os, math, statistics
os.system('cls')


print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")

a = (input("Enter value for a: "))
b = (input("Enter value for b: "))
c = (input("Enter value for c: "))

try:
  a = float(a)
  b = float(b)
  c = float(c)
except:
   print("Those are not valid values for a, b or c")
   exit()

try:
    r1 = round(((-b + (math.sqrt((b**2)-4*a*c)))/(2*a)),2)
    r2 = round(((-b - (math.sqrt((b**2)-4*a*c)))/(2*a)),2)
    if r1 == r2:
       print(f"The root is {r1}")
    else:
       print(f"The roots are {r1} and {r2}")
except:
   print("There are no real roots to the equation")

#done