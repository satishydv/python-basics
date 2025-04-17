print("welcome to the roller coster! ")
height = int(input("Enterr your height"))

if height >= 120:
    print("You can ride the roller coster !")
    age = int(input("What is your age"))

    if age < 12:
     bill = 5
     print("Please pay $5. ")
    elif age<=18:
        bill = 7
        print("Please pay $7. ")
    else:
        bill = 12
        print("Please pay $12")

    wants_photo = input("Do you want photo to be taken? Y or N. ")
    if wants_photo == "Y":
        # bill = bill + 3
        bill += 3
    
    print(f"Your final bill is {bill}")



else:
        print("Sorry,you have to grow taller before you can ride.")

       