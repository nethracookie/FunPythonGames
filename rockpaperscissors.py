#User inputs rock paper or scissors
#Computer generates a choice between the three options
#User is told if they win or lose
#Use random.randint to generate a random number. 
#Have 1 = rock, 2 = paper, 3 = scissors.
import random
rock = "The computer got rock."
paper = "The computer got paper."
scissors = "The computer got scissors."
user_query = input("Choose: 'Rock', 'Paper', or 'Scissors'")
win = "You win!"
tie = "Tie."
lose = "You lose."

print("Rock, Paper, Scissor ...shoot!")

a = random.randint(1, 3)
 
if a == 1 and user_query == 'Rock':
    print(rock, tie)
elif a == 1 and user_query == 'Paper':
    print(rock, win)
elif a == 1 and user_query == 'Scissors':
    print(rock, lose)
elif a == 2 and user_query == 'Rock':
    print(paper, lose)
elif a == 2 and user_query == 'Paper':
    print(paper, tie)
elif a == 2 and user_query == 'Scissors':
    print(paper, win)
elif a == 3 and user_query == 'Rock':
    print(scissors, win)
elif a == 3 and user_query == 'Paper':
    print(scissors, lose)
elif a == 3 and user_query == 'Scissors':
    print(scissors, tie)

print("Thanks for playing and come back soon!!")
