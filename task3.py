#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
number=float(input("Enter a number: "))
if number<0:
    print(str(number) + " is not a positive integer.")
    quit()
value=number%2
if value==1 or value==0 and number!=0:
    print(str(number) + ' is a positive integer.')
    quit()
if number==0:
    print("the number is zero. ")
