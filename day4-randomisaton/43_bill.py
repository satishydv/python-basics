# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# it already put item  in list
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)

number = len(names)
# print(number)

random_number = random.randint(0,number-1)
# print(random_number)

# print(names[random_number])

print(names[random_number],"need to pay the bill")

print(names[random_number] + " is going to buy the meal today!")

