tuple1 = (1, 2, 3, 4) # its a list with parenthesis, and it's IMMUTABLE!!!!
# tuples are faster than lists, so if you know it's not gonna change use it
tuple1[0] # 1
tuple1[3] # 4

tuple2 = (1,) #if it's just 1 value it needs a comma afterwards

#can be used as keys in dictionaries
# iterating is the same

set1 = set({1, 2, 3, 4, 5})

# no duplicates, no indexes, no keys, no values
# iterating is the same

#good way to remove duplicates

set1.add(6) # if the element is already there, you can't add anything
set1.remove(6)
# or
set1.discard(6) # if the element wasn't there at all, this won't throw an error

set2 = set1.copy()
set2.clear()

