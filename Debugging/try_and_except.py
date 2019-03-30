# handling errors

try: # we try something
   something # this throws an error cuz it doesn't exist
except NameError: # picks out the correct error
   print('error') # so instead of breaking the code, it prints the except
print('after the try') # and now the code can exist


try:
   num = int(input("please enter a number: "))
except TypeError:
   print("That's not a number")
else:
   print("This is ELSE") # will run if except doesn't run
finally:
   print("This will run no matter what")


def divide(a, b):
   try:
      result = a / b 
   except ZeroDivisionError:
      print("cant divide by 0")
   except TypeError:
      print("gotta be numbers")
   else:
      print(result)