'''Python Practice Set 1 (Beginners)

Q1: Your First Program
Write a program that prints:
Hello, World! Welcome to Python.'''

print("Hello, World! Welcome to Python.")

'''Q2: Print a Poem
Write a program that prints the following poem using a single print() statement:
(Hint: Use \n for a new line.)
Hello, World! Welcome to Python.
Twinkle, twinkle, little star,
How I wonder what you are! '''

print ("Hello, World! Welcome to Python.\nTwinkle, twinkle, little star, \nHow I wonder what you are! ")

'''Q3: Variables & Data Types
Create variables to store: - Your name (string)
- Your age (integer)
- Your height in meters (float)
- A boolean value representing whether you are a student
Print all of them in one line.'''

name ="Jack"
age =10
height=126.0
is_student=True
print(f"Hello I am {name}. I am {age} years old.My height is {height} cms  and I am a Student {is_student}")


'''Q4: Typecasting Practice
You are given a string:
num = "45"
Convert it into an integer and add 10 to it. Print the result.'''

num="45"
print("The conversion is :",int(num)+10)

'''Q5: Taking User Input
Write a program that:
Asks the user for their favorite food.
Prints:
Wow! I also like <food>.
'''

food = input("What is your favouritr food?")
print (f"Wow! I also like {food}")


'''Q7: Escape Sequences
Print the following output using escape sequences:
Jack said, "Python is awesome!"
This is on a new line.
This is a tab -> <- here '''

print ("Jack said, Python is awesome!\nThis is on a new line.\nThis is a tab \t here ")

'''Q8: Operator Challenge
Write a program that:
Takes an integer as input from the user.
Prints the square and cube of that number.'''

num = int(input("Enter a number:"))
print ("The Square of given number is:", num*num)
print ("The cube of given number is:", num*num*num)
