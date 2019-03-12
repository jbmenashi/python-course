age = input("How old are you?: ")
if age:
    if int(age) >= 21:
        print("You are good to enter and can drink")
    elif int(age) >= 18:
        print("You can enter but need a wristband")
    else:
        print("You can't come in")
else:
    print("Enter an age")
