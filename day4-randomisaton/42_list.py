# lists 
fruit = ["cherry", "Apple", " pear", "orange"]

# to print first fruit name put the index eg
print(fruit[0])

# in addition to using the positive index,so say 0, 1, 2, 3,you can also use a negative index.So if I wrote -1 or -2, 
# then it actually starts counting from the end of the list. So if I wrote fruits then i will get orange

print(fruit[-1])

# to change any index
fruit[3] = "lemon"
print(fruit)

# you could also add to the list
# append will add at the last of list

fruit.append("Mango")
print(fruit)