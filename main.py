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
import random
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
  print("YOU TYPED AN INVALID NUMBER!")
else:
  print(game_images[user_choice])

computer_choices = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choices])

if user_choice == 0 and computer_choices == 2:
	print("YOU WIN!")
elif user_choice == 2 and computer_choices == 1:
	print("YOU WIN!")
elif user_choice == 1 and computer_choices == 0:
	print("YOU WIN!")
elif computer_choices == 0 and user_choice == 2:
	print("YOU LOSE")
elif computer_choices == 2 and user_choice == 1:
  print("YOU LOSE")
elif computer_choices == 1 and user_choice == 0:
  print("YOU LOSE")
elif computer_choices == user_choice:
  print("IT IS A DRAW!")

