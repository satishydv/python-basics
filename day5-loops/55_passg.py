#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password =""

for char in range(1, nr_letters+1):
    random_char = random.choice(letters)
    password = password + random_char

for sym in range(1, nr_symbols+1):
    random_sym = random.choice(symbols)
    password = password + random_sym

for num in range(1, nr_numbers+1):
    random_num = random.choice(numbers)
    password = password + random_num
print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

T_password = []

for char in range(1, nr_letters+1):
    T_password.append(random.choice(letters))

for sym in range(1, nr_symbols+1):
    T_password.append(random.choice(symbols))
   

for num in range(1, nr_numbers+1):
    T_password.append(random.choice(numbers))


net = nr_letters + nr_symbols + nr_symbols
papword = ""
for n in range(0, net):
    random_n = random.choice(T_password)
    papword = papword + random_n

print(papword)




