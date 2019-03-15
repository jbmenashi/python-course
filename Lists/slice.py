list = [1, 2, 3, 4, 5]

list[1:] #slices from index 1 - the colon after means its a start index

list[:2] #slices UP TO index 2, does not include - colon before means its an end index

list[1:3] # you can have a start and end index

list[::2] # theres a third arg, its a step, it skips them

list[4::-1] # so this would count down from the end - it's a fancy reverse()
