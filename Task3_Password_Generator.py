# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))




str = ""
for x in range(nr_letters):
    y = random.randint(0, len(letters))
    str += letters[y]

sym = ""
for x in range(nr_symbols):
    z = random.randint(0, len(symbols) - 1)
    sym += symbols[z]

num = ""
for x in range(nr_numbers):
    a = random.randint(0, len(numbers) - 1)
    num += numbers[a]

password = str + sym + num
jumble = []
for x in password:
    jumble.append(x)

# print(jumble)
random.shuffle(jumble)
# print(jumble)
newpass = ""
for x in range(len(jumble)):
    newpass += jumble[x]

print(f"The password for you is: {newpass}")
