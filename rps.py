import sys #This enable us to use system exit to exit the program
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
#Rock paper scissors game
playerchoice = input("Enter...\n 1 for Rock, \n 2 for paper, or\n 3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3 :
    sys.exit("Pleae enter 1, 2, 0r 3.") #we have used system exit instead of print because we need to exit the program after it has been executed.

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("you chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😆 Draw...please play again")
else:
    print("😒 computer wins")