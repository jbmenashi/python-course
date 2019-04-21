file = open("test.txt") #save the file to a variable
file.read() #read the file - this puts the cursor at the end of the file

file.seek(0) #0 is the start, goes back to the beginning of the file so you can call read again

file.readline() #just reads the first line

file.readlines() #creates a list of every line, but preserves the lines

file.close() #closes the file, can't read it again until it's opened again