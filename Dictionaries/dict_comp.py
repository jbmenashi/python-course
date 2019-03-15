dict1 = {"first" : 1, "second" : 2, "third" : 3}

squared = {key: value ** 2 for key, value in dict1.items()}
cap = {key.upper(): value for key, value in squared.items()}

print(cap) #{"FIRST" : 1, "SECOND" : 4, "THIRD" : 9}

example2 = {num: num + 5 for num in [1,2,3,4,5]}

print(example2)


num_list = [1,2,3,4]

print({num: ("even" if num % 2 == 0 else "odd") for num in num_list})

list1 = [1, 2, 3]
list2 = [10, 20, 30]

combo = {list1[i]: list2[i] for i in range(0,3)}
