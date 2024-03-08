# Import the random module
import random

# Define lists of letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print welcome message and get user input for password criteria
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to store the password
password_list = []

# Generate random letters for the password based on user input
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

# Generate random symbols for the password based on user input
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

# Generate random numbers for the password based on user input
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# Shuffle the password list to randomize the order of characters
random.shuffle(password_list)

# Convert the password list into a string
password = ""
for char in password_list:
  password += char

# Print the generated password
print(f"Your password is: {password}")
