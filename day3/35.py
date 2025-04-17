# 🍕🍕Python pizza🍕🍕



# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
    bill = 15
    wants_pepperoni = input("Do you want a peperoni taken? Y or N. ")
    if wants_pepperoni == "Y":
     bill+= 2
elif size == "M":
    bill = 20
    wants_pepperoni = input("Do you want a peperoni taken? Y or N. ")
    if wants_pepperoni == "Y":
     bill+= 3
else:
    bill = 25
    wants_pepperoni = input("Do you want a peperoni taken? Y or N. ")
    if wants_pepperoni == "Y":
     bill+= 2

wants_chesse = input("Do you want a chesse? Y or N. ")
if wants_chesse == "Y":
    bill+= 1

print(f"Your final bill is ${bill}")





