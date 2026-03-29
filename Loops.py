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
reverse_string=''

for char in string:
    reverse_string=char + reverse_string
print(reverse_string)
