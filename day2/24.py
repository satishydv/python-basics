# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# since input always create string data type convert it

remain = 90 - int(age)
year = remain
months = remain*12
weeks = remain*52
days = weeks*7

print(f"you have {days} days, {weeks} weeks , and {months} months left ")