# given list of numbers,count how many numbers are positive
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_count = 0

for num in numbers:
    if num > 0:
        positive_num_count = positive_num_count + 1
print("The final positive numbers are:",positive_num_count)

# calculate sum of even numbers upto a given number n

number = int(input("Enter numbers:"))
sum_even = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        sum_even= sum_even+num
print ("The sum of even numbers is:", sum_even)        

# print multiplication table of a given number up to 10 but skip the fifth 
# iteration

num= int(input("Enter the number:"))

for i in range(1, 11):
    if i==5:
        continue
    print(num,'X',i,'=',num*i)

    #reverse a string using for loop
string = input("Enter a string:")
reverse_string = ''

for char in string:
    reverse_string = char + reverse_string
print(reverse_string)

# given a string find first non-repeated character in it.

string = input("Enter a string:")
repeated_char = ''

for char in string:
    if string.count(char) == 1:
        print('The first non-repeated character is:',char)
        break
# compute the factorial of a number using while loop
num1 = int(input("Enter number:"))
factorial = 1

while num1 > 0:
    factorial = factorial * num1
    num1 = num1 - 1

print('The factorial of given number is:',factorial)    

# keep asking the user for input until they enter a number between 1 and 10
num = int(input("Enter a number between 1 to 10:"))
while True:
    if  1<= num <=10:
        print('The entered number is',num)
        break
    else:
        print("Enter a valid number")   
        break
# check if number is prime or not
num = int(input("Enter a number :"))
is_prime = True
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
print(is_prime,)        

# check if elements of a list are unique. if duplicates are found exit the loop
# and print the duplicate items = ["apple", "banana", "orange", "apple", "grape"]

items = ["apple", "banana", "orange", "apple", "grape"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item:",item)
        break
    unique_item.add(item)