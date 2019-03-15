spurs = {"Eriksen", "Bale", "Kane", "Alli", "Modric"}
real = {"Ronaldo", "Ramos", "Bale", "Modric", "Benzema"}

print(spurs | real) # creates a Union of the 2 sets - that's everything in both with no duplicates
print(spurs & real) # creates an Intersection - so just Bale and Modric in this example