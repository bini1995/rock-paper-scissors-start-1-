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

#Write your code below this line 👇

player = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

bot = random.randint(0, 3)

print(player)
print(bot)

print("Player Chose: ")
if player == "0":
    print(rock)
elif player == "1":
    print(paper)
else:
    print(scissors)

print("Computer Chose: ")
if bot == 0:
    print(rock)
elif bot == 1:
    print(paper)
else:
    print(scissors)


if player == "0" and bot == 0:
    print("It's a draw, no one won. ")
elif player == "0" and bot == 1:
    print("Computer wins since rock beats paper")
elif player == "0" and bot == 2:
    print("Computer wins, since rock beats scissor")
elif player == "1" and bot == 1:
    print("It's a draw, no one won")
elif player == "1" and bot == 0:
    print("You won. ")
elif player == "1" and bot == 2:
    print("Computer won, since scissors beat paper. ")
elif player == "2" and bot == 0:
    print("Computer wins since rock beats scissors")
elif player == "2" and bot == 1:
    print("You win, since scissor beats paper")
elif player == "2" and bot == 2:
    print("It is a tie, Two papers.")
