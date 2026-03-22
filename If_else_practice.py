'''Write a program that asks the user for a number and prints whether it is
positive, negative, or zero.'''

num= int(input("Enter a number:"))

if num > 0 :
    print("The entered number is positive")
elif num ==0:
    print("The entered number is Zero")    
else :
    print("The entered number is Negative") 

'''Create a program that checks if a person is eligible to vote 
(age >= 18).'''

age = int(input("Enter the age:"))

if age >18:
    print("The person is eligible to vote")
elif age==18:
    print("The person is an Adult")
else:
    print("The person is not eligible to vote")

'''Write a program that takes a number from the user and prints “Even” if it is
even, otherwise “Odd”.'''

num=int(input("Enter a number:"))

if num %2 ==0:
    print("The entered number is even")
elif num==0:
    print("The entered number is Zero")
else :
    print("The entered number is odd")    
