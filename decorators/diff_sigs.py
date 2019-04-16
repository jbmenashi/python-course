def shout(fn):
   def wrapper(*args, **kwargs):
      return fn(*args, **kwargs).upper()
   return wrapper

@shout
def greet(name):
   return f"Hi, I'm {name}"

@shout
def order(main, side):
   return f"One {main} and a side of {side}"

print(greet("Bob"))
print(order("burger", "fries"))