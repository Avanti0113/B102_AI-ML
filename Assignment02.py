# 1. Even or Odd Function

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("1. Even or Odd:", is_even(6))


# 2. Largest of Two Numbers

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print("2. Largest Number:", largest(10, 20))


# 3. Print Numbers from 1 to n

def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

print("3. Numbers:")
print_numbers(5)


# 4. Sum of Numbers from 1 to n

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print("4. Sum:", sum_n(5))


# 5. Multiplication Table

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

print("5. Multiplication Table:")
table(5)


# 6. Count Even Numbers in a List

def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

print("6. Count Even:", count_even([1, 2, 3, 4, 6]))


# 7. Find Maximum Without Using max()

def find_max(numbers):
    largest_num = numbers[0]
    for n in numbers:
        if n > largest_num:
            largest_num = n
    return largest_num

print("7. Maximum:", find_max([10, 25, 5, 40, 15]))


# 11. FizzBuzz

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print("11. FizzBuzz:")
fizzbuzz()


# 12. Palindrome Checker

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print("12. Palindrome:", palindrome("madam"))


# 13. Count Vowels

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print("13. Vowels:", count_vowels("Hello World"))


# 14. Second Largest Number Without Using sort()

def second_largest(numbers):
    largest_num = float('-inf')
    second = float('-inf')

    for n in numbers:
        if n > largest_num:
            second = largest_num
            largest_num = n
        elif largest_num > n > second:
            second = n

    if second == float('-inf'):
        return None

    return second

print("14. Second Largest:", second_largest([10, 20, 5, 40, 30]))


# 15. Guessing Game

import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Correct! You won.")
            break
        else:
            print("Wrong guess. Try again!")

print("15. Guessing Game:")
# Uncomment the next line to play the game.
# guessing_game()


# 16. Grade Calculator

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print("16. Grade:", grade(85))