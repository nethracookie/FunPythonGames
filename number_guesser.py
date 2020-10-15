from random import randint
number = randint(1, 10)
while True:
    guess = int(input("What is your number between 1 and 10?"))
    if guess > number:
        print(guess, 'is too high!')
    elif guess < number:
        print(guess, 'is too low!')
    else:
        print(guess, "is correct!")
        break
print("Thanks for playing!")
