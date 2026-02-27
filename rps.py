# create a rock paper scissor game
import random

#3 options: rock, paper, scissors
choices = ["rock" ,"paper", "scissors"]
player_score = 0
computer_score = 0
print("Welcome to Rock, Paper, Scissors \n")

while True:
  # add a score
  print(f"Your score: {player_score} | Computer: {computer_score} \n")
# need to be able to take a users input so they can select
  player = input("choose either rock, paper, or scissors: ").lower()

if player == "quit":
    print("Thanks for playing!")
    break 

if player not in choices:
    print("That is not an option. Please choose either rock, paper, or scissors \n")
    continue
#need to give random choice to computer
computer = random.choice(choices) 
print("Your opponent chooses: ", computer)
# create what to do depending on different outcomes

if player == "rock" and computer == "scissors":
    print("You win rockstar!")
elif player == computer:
    print("oh - its a tie!\n")
elif player == "scissors" and computer == "paper":
    print("You are really cutting down your opponents! You Win!!!")
elif player == "paper" and computer == "rock":
    print("You win!!!\n")
else:
    print("haha - you lose! Better luck next time!")

           
