'''Ask the user to enter a day number (1–7) and print the corresponding day of
the week using match case .'''

num = int(input("Enter a number:"))

match num:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case 4:
        print("Today is Thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Enter a valid number between 1-7")

'''Write a program using match case that simulates a simple calculator.
Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case .'''       
    
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
operation = input("Enter a operation you want to perform:(+,-,*,/):")
    
match operation: 
    case "+":
        print("The sum of two number is:", num1+num2) 
    case "-":
        print("The Subtraction of two number is:", num1-num2) 
    case "*":
        print("The multiplication of two number is:", num1*num2) 
    case "/":
        print("The division of two number is:", num1/num2) 
    case _:
        print("Invalid operation")    
        


    
