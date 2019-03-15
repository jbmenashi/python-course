import random

play_again = ''
guess = None

while play_again != "n":
    random_number = random.randint(1, 10)
    while guess != random_number:
        guess = int(input("Guess a number between 1 and 10 "))
        if guess < random_number:
            print("Too Low")
        else:
            print("Too High")
    print("You Got It!")
    play_again = input("Play again? y/n ")
