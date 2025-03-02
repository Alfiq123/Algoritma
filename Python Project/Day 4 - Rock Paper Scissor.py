import random

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

# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:

visual = [rock, paper, scissors]

# player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

player_choice = 0
print(visual[player_choice])

computer_choice = random.randint(0, 2)
print(visual[computer_choice])

if player_choice > computer_choice:
    print("You Win")

if player_choice < computer_choice:
    print("You Lose")

if player_choice == computer_choice:
    print("It's Draw")
