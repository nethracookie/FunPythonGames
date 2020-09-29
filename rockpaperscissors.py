#User inputs rock paper or scissors
#Computer generates a choice between the three options
#User is told if they win or lose
#Use random.randint to generate a random number. Have 1 = rock, 2 = paper, 3 = sci.
import random

print("Welcome!!Rock,Paper,or Scissors??")

user = input("What do you say?")

print("Rock,Paper,Scissor ...shoot!")

a = random.randint(1, 3)
 
if a == 1:
    print("The computer got rock.")

if a == 2:
    print("The computer got scissors.")


if a == 3:
    print("The computer got paper.")


print("Thanks for playing and come back soon!!")