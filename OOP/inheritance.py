class Animal:
   def __init__(self, name, species):
      self.name = name
      self.species = species

   def __repr__(self):
      return f"{self.name} is a {self.species}"

   def make_sound(self, sound):
      print(f"this animal says {sound}")

class Cat(Animal):
   def __init__(self, name, breed):
      super().__init__(name, species="cat")
      self.breed = breed 

   def make_sound(self): #method overwriting
      return "Meow"


whiskers = Cat("Whiskers", "Tabby")
print(whiskers)
print(whiskers.make_sound())
print(whiskers.__dict__)
print(Cat.__mro__) # MRO is method resolution order, the order in which python looks for stuff - it's how you
#can do multiple inheritance