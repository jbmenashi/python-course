print("How many kilometers did you run today?")
kms = input() #takes in user input on command line
miles = float(kms)/1.60934 #float converts the type, could do int() or str()
print(f"That means you ran {round(miles, 2)} miles") #round takes 2 arguments, the thing and the decimals
