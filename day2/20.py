number = input("Type a two digit number \n")

# convert your two digit number in a string
str_num = str(number)

# we can access string letter using index
first_digit = str_num[0]
second_digit = str_num[1]

#again converting charachter into number
c = int(first_digit)
d = int(second_digit)

print(c+d)