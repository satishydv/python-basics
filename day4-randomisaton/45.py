# 🚨 Don't change the code below 👇
# row means column here and vice versa
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# print(map[1])  will print first row

horizontal = int(position[0])
vertical = int(position[1])

# selected_row = map[vertical-1]
# selected_row[horizontal-1] = "X"

# or

map[vertical-1][horizontal-1] = "X"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


