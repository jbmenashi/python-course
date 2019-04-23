
with open("write.txt", "w") as file:
   file.write("Look I'm writing in a file\n")

with open("write.txt", "a") as file:
   file.write("This won't get rid of the above text\n")








      

# with open("write.txt", "r+") as file:
#    file.seek(10)
#    file.write("LOOK AT ME")