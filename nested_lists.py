board = [["X" if num % 2 == 0 else "O" for num in range(1,4)] for val in range(1,4)]
#this is how to do list comp for a nested list
#the first part sets up what you want to do for an indiv list
#the second part essentially sets up how many times you want to do it
print(board)
