import random
list1 = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors")
player_wins = 0
comp_wins = 0
play_again = ''

while play_again != "n":
    while comp_wins < 2 and player_wins < 2:
        player = input("Player 1, enter choice: ")
        comp = random.choice(list1)
        print(f"computer chooses {comp}")
        if player == "rock" and comp == "paper" or player == "paper" and comp == "scissors" or player == "scissors" and comp == "rock":
            print("Computer wins!")
            comp_wins += 1
        elif comp == "rock" and player == "paper" or comp == "paper" and player == "scissors" or comp == "scissors" and player == "rock":
            print("You win!")
            player_wins += 1
        elif player == comp:
            print("Tie ballgame")
        else:
            print("Oops")
        print(f"Player: {player_wins}, Computer: {comp_wins}")
    if player_wins > comp_wins:
        print("Victory!")
    else:
        print("Defeat!")
    player_wins = 0
    comp_wins = 0
    play_again = input("Play Again? (y/n) ")
