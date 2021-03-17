#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_list = []

for x in range(nr_letters):
    total_list.append(letters)
for x in range(nr_symbols):
    total_list.append(symbols)
for x in range(nr_numbers):
    total_list.append(numbers)
total_num = nr_letters+nr_symbols+nr_numbers
password = ""

for x in range(total_num):
    list_index = random.randint(0,len(total_list)-1)
    list_character = total_list.pop(list_index)
    character = list_character[random.randint(0,len(list_character)-1)]
    password += character
    
print(f"Your password is: {password}")