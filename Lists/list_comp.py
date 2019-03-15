list = [1, 2, 3]

list2 = [x * 10 for x in list]

print(list)
print(list2)

# this kind of feels like a map function? it is

list3 = [x for x in list if x % 2 == 0] #so you can do conditionals as well like so

print(list3)

with_vowels = 'This is so much fun'

no_vowels = ''.join(char for char in with_vowels if char not in 'aeiou')

print(no_vowels)

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]] #[3, 4]

answer2 = [word.lower()[::-1] for word in ["Elie", "Tim", "Matt"]] #["eile", "mit", "ttam"]
