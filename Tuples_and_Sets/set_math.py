spurs = {"Eriksen", "Bale", "Kane", "Alli", "Modric"}
real = {"Ronaldo", "Ramos", "Bale", "Modric", "Benzema"}

print(spurs | real) # creates a Union of the 2 sets - that's everything in both with no duplicates
print(spurs & real) # creates an Intersection - so just Bale and Modric in this example


{x**2 for x in range(10)} # this is set comp, and it creates a set because you're not establishing a list or dict

{char.upper() for char in "hello"} # {L, E, H, O} - the order doesn't matter

{char for char in "hello" if char in "aeiou"} # so this would create a set of {e, o}