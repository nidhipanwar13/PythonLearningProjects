# write a function to calculate and return the square of a number

number = int(input("Enter a number:"))
def square_of_num(num):
    return num ** 2

result = square_of_num(number)
print("The square of given number is:",result)

# create a function that takes two numbers as parameters and returns their sum

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

def sum_of_num(a,b):
    return a+b

result = sum_of_num(num1,num2)
print("The sum of two numbers are:",result)

# write a function multiply that multiply two numbers but can also accepts and multiply strings


def multiply(a,b):
    return a * b

print('The multiplication is:',multiply(3,4))
print('The multiplication is:',multiply('hello',4))
print('The multiplication is:',multiply(3,'bye'))

# create a function that returns both the area and circumference of a circle given its radius

radius = float(input("Enter radius:"))

def circle_stats(r):
    area= 3.14 * r * r
    circumference = 2 * 3.14 * r
    return area,circumference
a , c = circle_stats(radius)
print('Area of circle is:',a)
print('Circumference of circle is:',c) 

# write a function that greets a user. If no name is provided, it should 
# greet with "Hello, Guest!"
guest = str(input("Enter name:"))

def greet(name = 'guest!'):
    return 'Hello' +' '+ name

print(greet())
print(greet(guest))

# create a lambda function to calculate the cube of a number
num = int(input('Enter number:'))
 
cube = lambda x : x ** 3 

print('Cube of number is:',cube(num))

# write a function that takes variable number of arguments and returns 
# their sum (using *args)