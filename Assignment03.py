# ==============================
# 1. DATA TYPES
# ==============================

# Q1. Find the data type of every value in a mixed list.

a = [10, 20.5, "Hello", True, 5, "Python"]

for i in a:
    print(i, type(i))


# Q2. Convert a nested list into a tuple of tuples.

a = [[1, 2], [3, 4], [5, 6]]
b = tuple(tuple(i) for i in a)
print(b)


# Q3. Remove all duplicate values from a mixed list while preserving the original order.

a = [10, "Hello", 20, 10, "Hello", 30, 20]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)


# ==============================
# 2. OPERATORS
# ==============================

# Q4. Check whether a number is a power of 2 using operators.

n = int(input("Enter number: "))

if n > 0 and (n & (n - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")


# Q5. Swap two numbers using bitwise XOR.

a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)


# Q6. Find whether a number is divisible by both 4 and 6 using logical operators.

n = int(input("Enter number: "))

if n % 4 == 0 and n % 6 == 0:
    print("Divisible by both 4 and 6")
else:
    print("Not divisible")


# Q7. Calculate the total electricity bill using different unit rates.

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5

print("Total Bill =", bill)


# ==============================
# 3. CONDITIONAL STATEMENTS
# ==============================

# Q8. Check whether three sides can form a triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Not a Triangle")


# Q9. Determine the type of triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")


# Q10. Create a simple ATM menu (Withdraw, Deposit, Balance).

balance = 5000

while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        amount = int(input("Enter amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
        else:
            print("Invalid Amount or Insufficient Balance")

    elif ch == 2:
        amount = int(input("Enter amount: "))
        if amount > 0:
            balance = balance + amount
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    elif ch == 3:
        print("Balance =", balance)

    elif ch == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")


# Q11. Calculate income tax based on different tax slabs.

income = int(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Income Tax =", tax)


# Q12. Create a menu-driven calculator using if-elif.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ch = int(input("Enter choice: "))

if ch == 1:
    print("Result =", a + b)
elif ch == 2:
    print("Result =", a - b)
elif ch == 3:
    print("Result =", a * b)
elif ch == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Choice")


# ==============================
# 4. LOOPS
# ==============================

# Q13. Print all prime numbers between 1 and n.

n = int(input("Enter number: "))

for i in range(2, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(i)


# Q14. Find the factorial of a number using a loop.

n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


# Q15. Print the Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()


# Q16. Check whether a number is an Armstrong number.

n = int(input("Enter number: "))

temp = n
total = 0
power = len(str(n))

while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


# Q17. Reverse a number and check if it is a palindrome.

n = int(input("Enter number: "))

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reverse =", rev)

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q18. Find the Greatest Common Divisor (GCD) of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", abs(a))


# ==============================
# 5. FUNCTIONS
# ==============================

# Q19. Write a function to check if a string is a palindrome.

def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

s = input("Enter string: ")
palindrome(s)


# Q20. Write a function to count vowels and consonants in a string.

def count_letters(s):
    vowels = 0
    consonants = 0

    for i in s.lower():
        if i.isalpha():
            if i in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels =", vowels)
    print("Consonants =", consonants)

s = input("Enter string: ")
count_letters(s)


# Q21. Create a function to calculate simple and compound interest.

def interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * (1 + r / 100) ** t - p

    print("Simple Interest =", si)
    print("Compound Interest =", ci)

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

interest(p, r, t)


# Q22. Write a function to return all factors of a number.

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

n = int(input("Enter number: "))
factors(n)
print()


# Q23. Write a function to find the second-largest number in a list.

def second_largest(a):
    a = list(set(a))
    a.sort()

    if len(a) >= 2:
        print("Second Largest =", a[-2])
    else:
        print("Not Enough Elements")

a = [10, 20, 40, 30, 40]
second_largest(a)


# ==============================
# 6. LISTS
# ==============================

# Q24. Merge two lists without duplicates.

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = []

for i in a + b:
    if i not in c:
        c.append(i)

print(c)


# Q25. Find the second-largest and second-smallest elements.

a = [10, 20, 30, 40, 50]
b = sorted(set(a))

if len(b) >= 2:
    print("Second Smallest =", b[1])
    print("Second Largest =", b[-2])
else:
    print("Not Enough Elements")


# Q26. Rotate a list to the left by k positions.

a = [1, 2, 3, 4, 5]
k = int(input("Enter k: "))

k = k % len(a)
b = a[k:] + a[:k]

print(b)


# Q27. Separate even and odd numbers into two lists.

a = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even =", even)
print("Odd =", odd)


# Q28. Find the common elements between two lists.

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)

print("Common Elements =", c)


# ==============================
# 7. TUPLES AND SETS
# ==============================

# Q29. Count the frequency of each element in a tuple.

a = (1, 2, 3, 2, 1, 4, 2)

for i in set(a):
    print(i, "=", a.count(i))


# Q30. Find the union, intersection, and difference of two sets.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union =", a | b)
print("Intersection =", a & b)
print("Difference =", a - b)


# Q31. Check whether one set is a subset of another.

a = {1, 2}
b = {1, 2, 3, 4}

if a.issubset(b):
    print("A is subset of B")
else:
    print("A is not subset of B")


# ==============================
# 8. DICTIONARIES
# ==============================

# Q32. Count the frequency of words in a sentence.

s = input("Enter sentence: ")
words = s.split()
d = {}

for i in words:
    d[i] = d.get(i, 0) + 1

print(d)


# Q33. Create a dictionary from two lists (keys and values).

keys = ["Name", "Age", "City"]
values = ["Avantika", 21, "Pune"]

d = dict(zip(keys, values))

print(d)


# Q34. Sort a dictionary by its values.

d = {"A": 30, "B": 10, "C": 20}

s = dict(sorted(d.items(), key=lambda x: x[1]))

print(s)


# ==============================
# 9. FILE HANDLING
# ==============================

# Q35. Read a text file and count the number of lines, words, and characters.

f = open("data.txt", "r")
data = f.read()

lines = data.splitlines()
words = data.split()
characters = len(data)

print("Lines =", len(lines))
print("Words =", len(words))
print("Characters =", characters)

f.close()


# Q36. Copy only the even-numbered lines from one file to another.

f = open("data.txt", "r")
g = open("even.txt", "w")

for i, line in enumerate(f, start=1):
    if i % 2 == 0:
        g.write(line)

f.close()
g.close()

print("Even lines copied successfully")


# ==============================
# 10. EXCEPTION HANDLING
# ==============================

# Q37. Handle invalid integer input using try-except.

try:
    n = int(input("Enter number: "))
    print("Number =", n)

except ValueError:
    print("Please enter a valid integer")


# Q38. Handle file-not-found errors while reading a file.

try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File Not Found")


# ==============================
# 11. MODULES
# ==============================

# Q39. Create a random password generator using random and string modules.

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(8):
    password = password + random.choice(characters)

print("Password =", password)


# Q40. Use datetime module to calculate the number of days between two dates.

from datetime import date

d1 = date(2026, 1, 1)
d2 = date(2026, 11, 4)

difference = d2 - d1

print("Number of Days =", difference.days)