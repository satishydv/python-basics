# BMI calculator 2.0
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight/(height**2)
print(f"Your bmi is {bmi}")

if bmi < 18.5:
         print("fYour bmi is {bmi}, underweight. ")
elif bmi<=25:
        print("normal weight. ")
elif bmi<=30:
        print("overweight. ")
elif bmi<=35:
        print("obese. ")
else:
        print("clinically obese")
