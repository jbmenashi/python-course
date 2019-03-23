# ALL returns True if everything in an iterable is truthy
all([1, 2, 3]) # True

# ANY returns True if anything in an iterable is truthy
any([0, 0, 0, 1]) # True

# If you just want a boolean  - you can do a Generator Expression - it's just a list comp without brackets, saves memory

import sys
print(sys.getsizeof("something"))

#SORTED sorts stuff, can take in a key (a value to sort a dictionary by) and reverse boolean
sorted([3, 7, 1, 10, 2]) # [1, 2, 3, 7, 10]
sorted([3, 7, 1, 10, 2], reverse=True)

users = ["Bob,", "Tim"]
sorted(users, key=lambda user: len(user["name"]), reverse = True)

# MIN and MAX, duh

min(1, 2, 3) # 1
min([4, 5, 6]) # 4

names = ["Bob", "Tim", "Jonesy"]
max(len(name) for name in names) # Jonesy - its a generator, not a list comp, but same idea

reversed([1, 2, 3, 4]) #reverses it, but just use the cool slide method

"".join(list(reversed("hello"))) #olleh

abs(-3) #duh


sum([1, 2, 3]) # adds them up! Helpful
sum([1, 2, 3], 10) # the second arg is a start, so this would be 16

round(10.1234) # 10
round(10.1234, 2) # 10.12, the second arg is the digits you want
