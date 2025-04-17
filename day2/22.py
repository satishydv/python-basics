# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# since input function store default in string

bmi = int(weight) / float(height) ** 2
print(bmi)
result = round(bmi)
print("Your bmi is" ,result)








