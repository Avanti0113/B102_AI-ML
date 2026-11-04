# Q1. Write a Python program to check whether a number is even or odd.

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Q2. Write a program to find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)


# Q3. Write a program to check whether a given number is prime.

n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime")


# Q4. Write a program to print the Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print()


# Q5. Write a program to find the factorial of a number using a loop.

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


# Q6. Write a program to reverse a string without using [::-1].

s = input("Enter a string: ")
rev = ""

for i in s:
    rev = i + rev

print("Reverse String =", rev)


# Q7. Write a program to check whether a string is a palindrome.

s = input("Enter a string: ")
rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q8. Write a program to count the number of vowels and consonants in a string.

s = input("Enter a string: ")
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


# Q9. Write a program to find the sum of all elements in a list.

a = [10, 20, 30, 40, 50]
total = 0

for i in a:
    total = total + i

print("Sum =", total)


# Q10. Write a program to find the largest and smallest element
# in a list without using max() or min().

a = [10, 50, 20, 5, 40]

largest = a[0]
smallest = a[0]

for i in a:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)


# Q11. Write a program to remove duplicate elements from a list.

a = [10, 20, 30, 10, 20, 40]
b = []

for i in a:
    if i not in b:
        b.append(i)

print("List without duplicates =", b)


# Q12. Write a program to count how many times each element
# appears in a list using a dictionary.

a = [10, 20, 10, 30, 20, 10]
d = {}

for i in a:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print("Frequency =", d)


# Q13. Write a program to find the second-largest number in a list.

a = [10, 20, 40, 30, 50]
a = list(set(a))
a.sort()

if len(a) >= 2:
    print("Second Largest =", a[-2])
else:
    print("Second largest does not exist")


# Q14. Write a program to sort a list without using sort() or sorted().

a = [50, 20, 40, 10, 30]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("Sorted List =", a)


# Q15. Write a function that accepts a list of numbers
# and returns a list containing only the even numbers.

def even_numbers(a):
    b = []

    for i in a:
        if i % 2 == 0:
            b.append(i)

    return b

a = [1, 2, 3, 4, 5, 6, 7, 8]
print("Even Numbers =", even_numbers(a))


# Q16. Write a program to find the frequency of each character in a string.

s = input("Enter a string: ")
d = {}

for i in s:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print("Character Frequency =", d)


# Q17. Write a program to check whether two strings are anagrams.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagram")
else:
    print("Not Anagram")


# Q18. Write a program to find all duplicate values in a list.

a = [10, 20, 30, 10, 40, 20, 50]
duplicate = []

for i in a:
    if a.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print("Duplicate Values =", duplicate)


# Q19. Write a program that takes a sentence and finds the longest word.

s = input("Enter a sentence: ")
words = s.split()
longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest Word =", longest)


# Q20. Create a simple student marks program that:
# 1. Accepts marks for 5 subjects.
# 2. Calculates total and percentage.
# 3. Assigns a grade.
# 4. Displays whether the student passed or failed.

marks = []

for i in range(5):
    m = int(input("Enter subject marks: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage, "%")

if any(m < 35 for m in marks):
    print("Result = Fail")
elif percentage >= 90:
    print("Grade = A")
    print("Result = Pass")
elif percentage >= 75:
    print("Grade = B")
    print("Result = Pass")
elif percentage >= 60:
    print("Grade = C")
    print("Result = Pass")
elif percentage >= 35:
    print("Grade = D")
    print("Result = Pass")