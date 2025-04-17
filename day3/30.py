print("welcome to the roller coster! ")
height = int(input("Enterr your height"))

if height >= 120:
    print("You can ride the roller coster !")
    age = int(input("What is your age"))

    if age < 12:
         print("Please pay $5. ")
    elif age<=18:
        print("Please pay $7. ")
    else:
        print("Please pay $12")


else:
        print("Sorry,you have to grow taller before you can ride.")

        # if and else should be at same level otherwise it would cause indentation error and print not same level as of if
        # elif means else if
        # elif here will catch every condition btw 12 and 18