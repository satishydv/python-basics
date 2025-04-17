rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user = input(f"What do you choose? Type 0  for Rock, 1 for Paper or 2 for Scissors.")
user = int(user)

images = [rock,paper,scissors]

import random

computer = random.randint(0,2)
print(images[computer])

if user == 0 and computer == 2:
    print(images[user])
    print("You win")

elif user == 2 and computer == 0:
    print(images[user])
    print("computer win")

elif user > computer:
    print(images[user])
    print("You win")

elif user >= 3 or user < 1:
    print(images[user])
    print("You win")

elif computer > user:
    print(images[user])
    print("computer win")

else:
    print("its a draw")