#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Initialize the variables to string
r_letters = ""
r_symbol = ""
r_numbers = ""
#random generator letters
for Pick_Letter in range (0,nr_letters):
    r_letters += random.choice(letters)
#random generator symbols
for Pick_Symbols in range (0,nr_symbols):
    r_symbol += random.choice(symbols)
#random generator numbers
for Pick_Numbers in range(0,nr_numbers):
    r_numbers +=random.choice(numbers)
#Convert STRING to LIST
shuffle = r_letters + r_symbol + r_numbers
str_var = list(shuffle)
#Randomizer List
random.shuffle(str_var)
print ('Your random password is : '"".join(str_var))
print (" ".join(str_var))



