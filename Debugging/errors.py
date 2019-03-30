# Use the keyword "raise" to raise an error

# raise NameError("this would raise a name error")

def colorize(text, color):
   colors = ("cyan", "yellow", "magenta")
   if type(text) is not str:
      raise TypeError('Text must be a string')
   if color not in colors:
      raise ValueError('invalid color')
   print( f"{text} in {color}")

colorize([], "cyan") #Type Error
colorize("hello", "blue") # Value Error
colorize("hello", "cyan") # works