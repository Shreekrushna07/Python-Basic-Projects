# Importing the logo from the art module
from art import logo

# The alphabet used for the Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to perform the Caesar cipher
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  # If the direction is 'decode', reverse the shift amount to decrypt the message
  if cipher_direction == "decode":
    shift_amount *= -1
  # Loop through each character in the start_text
  for char in start_text:
    # If the character is in the alphabet, encrypt/decrypt it
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      # If the character is not in the alphabet, keep it as it is
      end_text += char
  # Print the result
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Print the logo
print(logo)

# Flag to control the loop
should_end = False
while not should_end:
  # Input the direction (encode or decode)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  # Input the message to be encrypted/decrypted
  text = input("Type your message:\n").lower()
  # Input the shift amount
  shift = int(input("Type the shift number:\n"))
  # Ensure the shift amount is within the range of the alphabet
  shift = shift % 26

  # Call the caesar function with the input values
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  # Ask the user if they want to go again
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    # If the user does not want to go again, set should_end to True and print goodbye
    should_end = True
    print("Goodbye")
