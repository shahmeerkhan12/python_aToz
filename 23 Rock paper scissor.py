#the rock paper scissor Game
import random
# this loop will help us to let user if he wants to play again or quit

while True:
   choices = ["rock", "paper", "scissor"]

   computer=random.choice(choices)
   # to prevent the player from inputing some other non relevant options/choices
   player=None

   while player not in choices:
      player = input("rock, paper, or scissor?:").lower()

   if computer == player :
         print("computer is: "+computer)
         print("player is: "+player)
         print("Tie!!")

   elif player == "rock" :
      if computer =="scissor" :
         print("computer is: "+computer)
         print("player is: "+player)
         print("you win!!")
      if computer =="paper" :
         print("computer is: "+computer)
         print("player is: "+player)
         print("you lose!!")

   elif player == "scissor" :
      if computer =="rock" :
         print("computer is: "+computer)
         print("player is: "+player)
         print("you lose!!")
      if computer =="paper" :
         print("computer is: "+computer)
         print("player is: "+player)
         print("you win!!")

   elif player == "paper" :
      if computer =="rock" :
         print("computer is: "+computer)
         print("player is: "+player)
         print("you win!!")
      if computer =="scissor" :
         print("computer is: "+computer)
         print("player is: "+player)
         print("you lose!!")

   play_again = input("Want to play again(yes/no)?: ").lower()
   if play_again!= "yes":
      break 

print("ByeBye!!")