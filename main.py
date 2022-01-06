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
Pmoves = [rock, paper, scissors]

move = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if move < 0 or move >= 3:
    print("You typed in an invalid choice. You lose.")
else:
    print(Pmoves[move])
    computer = random.randint(0, 2)
    print(f"Computer chose: \n {Pmoves[computer]}")

    if move == 0 and computer == 1:
        print("You lost.")

    elif move == 0 and computer == 2:
        print("You won.")

    elif move == 0 and computer == 0:
        print("It's a draw.")

    if move == 1 and computer == 1:
        print("Its a draw.")

    elif move == 1 and computer == 2:
        print("You lost.")

    elif move == 1 and computer == 0:
        print("You lost.")

    if move == 2 and computer == 1:
        print("You won.")

    elif move == 2 and computer == 2:
        print("its a draw")

    elif move == 2 and computer == 0:
        print("You lost.")
