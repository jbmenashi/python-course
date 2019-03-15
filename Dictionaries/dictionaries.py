dict1 = {"name" : "Jacob", "age" : 25, "eyes" : "blue"}

for value in dict1.values(): #how to get the values
    print(value)

for key in dict1.keys(): #how to get the keys
    print(key)

for key, value in dict1.items():
    print(key, value) # get all the key-value pairs

"name" in dict1 #true
"Jacob" in dict1.values() #true
