# 1. Check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Find the greater of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greater:", a)
elif b > a:
    print("Greater:", b)
else:
    print("Both are equal")


# 4. Find the greatest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)


# 5. Check if a person is eligible to vote
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 6. Check whether a year is a leap year
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


# 7. Check if a character is a vowel or consonant
ch = input("Enter a character: ")
if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# 8. Check whether a number is divisible by 5 and 11
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# 9. Check if a number is a multiple of both 3 and 7
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")


# 10. Assign grades based on marks
marks = float(input("Enter marks: "))
if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade D")
elif marks < 60:
    print("Grade F")
else:
    print("Invalid marks")


# 11. Check if a character is uppercase or lowercase
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an alphabet")


# 12. Find whether entered alphabet is a vowel using if-elif
ch = input("Enter an alphabet: ").lower()
if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Consonant")


# 13. Check if three sides can form a triangle
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Can form a triangle")
else:
    print("Cannot form a triangle")


# 14. Determine the type of triangle
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# 15. Find the largest among four numbers
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d

print("Largest:", largest)


# 16. Check whether a number is a three-digit number
num = int(input("Enter a number: "))
if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# 17. Calculate electricity bill using slab rates
units = float(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Electricity Bill:", bill)


# 18. Calculate income tax based on income slabs
income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20
else:
    tax = 112500 + (income - 1000000) * 0.30

print("Income Tax:", tax)


# 19. Check if a student passes
marks1 = int(input("Enter subject 1 marks: "))
marks2 = int(input("Enter subject 2 marks: "))
marks3 = int(input("Enter subject 3 marks: "))

if marks1 >= 35 and marks2 >= 35 and marks3 >= 35:
    print("Pass")
else:
    print("Fail")


# 20. Find whether a number is within a given range
num = int(input("Enter number: "))
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

if lower <= num <= upper:
    print("Number is within the range")
else:
    print("Number is outside the range")


# 21. Simple calculator using if-elif-else
a = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = int(input("Enter second number: "))

if operator == '+':
    print("Result:", a + b)
elif operator == '-':
    print("Result:", a - b)
elif operator == '*':
    print("Result:", a * b)
elif operator == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# 22. Check if a year is a century leap year
year = int(input("Enter year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
else:
    print("Not a century leap year")


# 23. Determine the season based on month number
month = int(input("Enter month number (1-12): "))

if month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
elif month in [12, 1, 2]:
    print("Winter")
else:
    print("Invalid month")


# 24. Find the number of days in a month
month = int(input("Enter month number: "))

if month == 2:
    print("28 or 29 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
else:
    print("Invalid month")


# 25. Check whether a password meets minimum conditions
password = input("Enter password: ")

has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Valid password")
else:
    print("Invalid password")


# 26. Determine ticket price based on age category
age = int(input("Enter age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 50
elif age <= 59:
    price = 100
else:
    price = 60

print("Ticket Price:", price)


# 27. Calculate discount based on purchase amount
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.15
elif amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Amount:", final_amount)


# 28. Check eligibility for driving license
age = int(input("Enter age: "))
eyesight = input("Do you have normal eyesight? (yes/no): ").lower()

if age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")


# 29. Login system with username and password validation
correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")


# 30. Menu-driven calculator
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    elif choice == 5:
        print("Program exited")
        break

    else:
        print("Invalid choice")