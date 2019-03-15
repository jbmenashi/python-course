list = [1, 2, 3, 4, 5]

list.append(6) #adds to the end of the list, takes only 1 arg
list.extend([7, 8]) #adds as many as you want

list2 = [9, 10, 11]
list.extend(list2) #so it's kind of like concat

list.insert(2, 2.5) #index, value

list2.clear() #duh

list.pop() #removes the last item
list.pop(2) #you can also put in an argument for the index, and returns the item

list.remove(10) #removes first VALUE that matches the arg, not the index

print(list)
