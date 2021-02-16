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
number = input("please enter a number")
number=float(number)
a= (number>=0)

if number==int(number) and number>=a:
    print(str(number)+"is a positive integer")
else:
    print(str(number)+ "is not a positive integer")