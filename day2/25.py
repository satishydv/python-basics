print("Welcome to the tip calculator")

net = input("What was the total bill $ \n")
net = float(net)

percentage = input("what % tip would you like to give ?")
percentage = float(percentage)

cont = input("How many people to split the bill ?")

a = net*(percentage/100)
b = a/4

print(round(b,2))  
