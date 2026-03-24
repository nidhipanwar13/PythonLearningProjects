'''Print numbers from 1 to 10 using a while loop.'''

sum=0
i=1
while i < 10:
    sum=sum+i
    i=i+1
    print(sum)


'''Write a program that keeps asking the user to enter a password until they
enter the correct one.'''

password= 'Happy123'

entered_pass= str(input("Enter the password:"))
while entered_pass != password:
    entered_pass = input("Incorrect password. Please try again: ")

print('password is correct')

'''Use a while loop to reverse a given number (e.g., 123 → 321).'''
num=123

print("The Reverse String is:",str(num)[::-1])