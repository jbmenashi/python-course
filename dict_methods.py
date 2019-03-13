dict1 = {"name" : "Jacob", "age" : 25, "eyes" : "blue"}

dict2 = dict1.copy() # makes a clone - not equal in memory

dict2.clear() # clears it

{}.fromkeys("a", "b") # creates a key value pair in a new dict {"a" : "b"}
{}.fromkeys([1, 2, 3, 4, 5], "number")

dict1.get("name") # Jacob
dict1.get("blah") # None

dict1.pop("eyes") # Removes it, but you NEED an arg, doesn't just auto do the last one

dict1.popitem() # Removes something RANDOM, no arg

dict2.update(dict1) # not sure why you would use this
