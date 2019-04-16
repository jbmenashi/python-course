def sum(n, func):
   total = 0
   for num in range(1, n + 1):
      total += func(num)
   return total

def square(x):
   return x * x

print(sum(3, square))

def make_laugh_at(person):
   def get_laugh():
      laugh = "Ha"
      return f"{laugh} {person}"
   return get_laugh #this is returning the function

laugh_at = make_laugh_at("Bob") #saving the return to a variable

print(laugh_at()) #so you need to call the function again