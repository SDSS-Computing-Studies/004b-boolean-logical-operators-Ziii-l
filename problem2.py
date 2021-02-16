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
a = int(input("please enter a number"))
b = int(input("please enter another number"))

if a >= b and a % b== 0：
print(str(a)+" is a factor of"+ str(b)) 
elif a <= b and b % a ==0:
    print(str(b)+" is a factor of"+ str(a))         
else:
    print (str(a)+" is not a factor of"+ str(b)) or print(str(b)+" is not a factor of"+ str(a))  