#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
number=int(input("Enter a number: "))
cube=number**(1/3)
square=number**0.5
sq2=square%2
c2=cube%2
if (sq2==1 or sq2==0) and (c2==1 or c2==0):
    print(str(number) + " is both a perfect square and a perfect cube.")
elif sq2!=1 and sq2!=0 and c2==1 or c2==0:
    print(str(number) + " is only a perfect cube.")
elif sq2==1 or sq2==0 and c2!=1 and c2!=0:
    print(str(number) + " is only a perfect square.")
