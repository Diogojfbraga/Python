# LOOP

# Example of iterating over a list of fruits
fruits = ["Apple", "Banana", "Pear"]
for fruit in fruits:
    print(fruit)

# List of student scores
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

# Calculate the sum of all student scores
sum = 0
for student in student_scores:
    sum += student
print(sum)

# Find the maximum score
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

# RANGE

# Calculate the sum of numbers from 1 to 100
sum = 0
for number in range(1, 101):
    sum += number
print(sum)

# FizzBuzz implementation: Print numbers from 1 to 100
# If divisible by 3 → print "Fizz", if divisible by 5 → print "Buzz", if both → print "FizzBuzz"
numbers = 0
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
        print(number)
    elif number % 3 == 0:
        number = 'Fizz'
        print(number)
    elif number % 5 == 0:
        number = 'Buzz'
        print(number)
    else:
        print(number)

import string
import random

# Lists of characters for password generation
letters = [char for char in string.ascii_lowercase]  # List of lowercase letters: ['a', 'b', 'c', ..., 'z']
numbers = [char for char in string.digits]  # List of digits: ['0', '1', '2', ..., '9']
symbols = [char for char in string.punctuation]  # List of special characters: ['!', '@', '#', '$', '%', '&', '*', ...]

# Display available characters
# print("letters =", letters)
# print("numbers =", numbers)
# print("symbols =", symbols)

print("Welcome to the PyPassword Generator!")

# Get user input for password criteria
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy level password generation (without shuffling)
password = []

# Add random letters to the password
for letter in range(0, nr_letters):
    password.append(random.choice(letters))

# Add random numbers to the password
for number in range(0, nr_numbers):
    password.append(random.choice(numbers))

# Add random symbols to the password
for symbol in range(0, nr_symbols):
    password.append(random.choice(symbols))

# Print the unshuffled password
# print(password)

# Shuffle the password characters for randomness
random.shuffle(password)

# Convert shuffled list back into a string
new_password = ''
for letter in password:
    new_password += letter

# Print the final shuffled password
print(f"Your password is: '{new_password}'")
