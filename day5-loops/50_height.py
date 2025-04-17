# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# so split seprated by space
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
for height in student_heights:
  total_height = total_height + height
print(total_height)

n = 0
for student in student_heights:
    n = n+1
print(n)

avg = round(total_height/n)
print(avg)


