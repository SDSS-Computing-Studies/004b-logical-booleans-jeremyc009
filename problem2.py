#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
number1=int(input("Enter an integer "))
number2=int(input('Enter another integer '))
if (number1>number2)==True:
    gNum=number1
    lNum=number2
else:
    gNum=number2
    lNum=number1
value=gNum%lNum
if value==0:
    print(str(lNum) + " is a factor of " + str(gNum))
else: 
    print(str(lNum) + " is not a factor of " + str(gNum))