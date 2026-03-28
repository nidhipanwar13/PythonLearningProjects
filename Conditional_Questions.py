# problem:movie ticket are priced as follows:
# $12 for adults (18 or older)
# $8 for children (under 18).
#evryone gets a $2 discount on wednesday. 
# Write a program that asks the user for their age and the day of the week, then calculates and prints the price of their movie ticket.

age = int(input("Enter Age of a person:"))
day = input("Enter day:")

# if day == "Wednesday":
#     if age >= 18:
#         print("The price of movie ticket is $10")
#     else:
#         print("The price of movie ticket is $6")
# else:
#     if age >= 18:
#         print("The price of movie ticket is $12")
#     else:
#         print("The price of movie ticket is $8")   

price = 12 if age >= 18 else 8
if day == 'Wednesday':
    price=price-2
    print("The price of movie ticket is $",price)

#Assign a grade (A, B, C, D, F) to a student based on their 
# score (90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F).

grade = int(input("Enter Number of a student:")) 

if grade >+ 101 :
    print("Please provide valid grade beween 0 to 100")
    exit()

if grade >= 90:
    print("The student got 'A' grade")
elif grade >= 80:
    print("The student got 'B' grade") 
elif grade >= 70:
    print("The student got 'C' grade")
elif grade >= 60:
    print("The student got 'D' grade") 
else:
    print("The student got 'F' grade")     

 # derrmine if a fruit is ripe,unripe, or overripe based on its
 #  color (banana e.g., green: unripe, yellow: ripe, brown: overripe).

fruit  = input ("Enter fruit:")
colour = input("Enter colour:")

if fruit == 'Banana' :
    if colour == 'green':
        print("The fruit is unripe ")
    elif colour == 'yellow':
        print("The fruit is ripe")   
    elif colour == 'brown':
        print("The fruit is overripe")  

if fruit == 'Apple' :
    if colour == 'green':
        print("The fruit is unripe ")
    elif colour == 'yellow':
        print("The fruit is ripe")   
    elif colour == 'brown':
        print("The fruit is overripe")  
else:
    print("Enter a valid fruit")    

# suggest an activity based on the weather (e.g., sunny: go for a
#  walk, rainy: stay indoors, snowy: build a snowman).

weather_con = input("Enter weather condition:")

if weather_con == 'sunny':
    print("Go for a walk")
elif weather_con == 'rainy':
    print("Stay Indoor")
elif weather_con == 'snowy':
    print("build a Snowman") 

#choose a mode of transportation based on the distance to be 
# traveled (e.g., <3km: walk, 3-15km: bike, >15km: car).

distance = int (input("Enter distance in Kms:"))
if distance < 3:
    print("Go for a Walk")
elif distance <=15 :
    print("take Bike") 
else:
    print("Take car")  

# check if password is weak (less than 6 characters),
# medium (6-10 characters), or strong (more than 10 characters). 

password = input("Enter password:")

if len(password) < 6:
    print("Password is weak")
elif len(password) <= 10:
    print("Password is medium")
else:
    print("Password is strong")

# determine if year is a leap year (divisible by 4 but not by 100, unless
# also divisible by 400).

year = int(input("Enter year:"))

if (year % 4==0 and year % 100 !=0) or (year % 400 ==0):
    print("leap year")
else:
    print("Not a leap year")    