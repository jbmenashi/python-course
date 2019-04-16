def lets_go(func):
   def wrapper():
      print("Let's go")
      func() #calls the passed-in function after the print
   return wrapper #returning the inner function

@lets_go #this is a decorator, it implies that the following function IS that passed-in function

def red_sox():
   print('Red Sox')

red_sox() #prints out "let's go Red Sox"