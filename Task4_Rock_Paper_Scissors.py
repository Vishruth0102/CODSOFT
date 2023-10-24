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

# Write your code below this line 👇
rounds = int(input("How many points do you want to play this game for?"))
for x in range(rounds * 10):

    game = [rock, paper, scissors]
    n = random.randint(0, 2)

    user = int(input(
        "what is your choice?\n 1.Rock\n 2.Paper\n 3.Scissors\n Please type the number corresponding to your choice.\n"))
    computer = game[n]
    countP = 0
    countC = 0
    print("Player:\n" + game[user - 1])
    print("Opponent:\n" + computer)
    if n == 0 and user == 1:
        print("It's a draw!")
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    elif n == 0 and user == 2:
        print("Player wins!")
        countP += 1
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    elif n == 0 and user == 3:
        print("Computer wins!")
        countC += 1
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    elif n == 1 and user == 1:
        print("Computer wins!")
        countC += 1
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    elif n == 1 and user == 2:
        print("It's a draw!")
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    elif n == 1 and user == 3:
        print("Player wins!")
        countP += 1
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    elif n == 2 and user == 1:
        print("Player wins!")
        countP += 1
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    elif n == 2 and user == 2:
        print("Computer wins!")
        countC += 1
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    elif n == 2 and user == 3:
        print("It's a draw!")
        print(f"The Player's points are {countP}")
        print(f"The Computer's points are {countC}")
    else:
        print("Please follow the instructions on the screen properly.")

    if countC == rounds or countP == rounds:
        break

    else:
        pass
if countC > countP:

    print("\n\n\n")
    print(
        "--------------------------------------------------------------------------------------------------------------------------------------")
    print("The Computer is the winner!")
    print(f"The Player's points are {countP}")
    print(f"The Computer's points are {countC}")
else:
    print("\n\n\n")
    print(
        "--------------------------------------------------------------------------------------------------------------------------------------")
    print("The Player is the winner!")
    print(f"The Player's points are {countP}")
    print(f"The Computer's points are {countC}")


