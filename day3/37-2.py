print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You are at cross road where do you want to go Left or Right")
lc_direction = direction.lower()

if lc_direction == "left":
    nxt = input('You have come to lake there is a island in middle of lake type "wait" to wait for boat or"swim" to swim by yourself')
    lc_nxt = nxt.lower()

    if lc_nxt == "wait":
        nxt2 = input("Which door")
        lc_nxt2 = nxt2.lower()

        if lc_nxt2 == "red":
            print("Game over")

        elif lc_nxt2 == "blue":
            print("Game over")

        else:
            print("you win")   

    else:
     print("Game over")



else:
    print("You fell into a hole. Game over")