# to add even btw 1 and 100
sum = 0
for number in range(1,101):
    if number%2 == 0:
        sum = sum + number
print(sum)

#or

sum2 = 0
for number in range(2,101,2):
    sum2 = sum2+number
print(sum2)
