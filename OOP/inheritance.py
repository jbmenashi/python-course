class Animal:
   def __init__(self, name, species):
      self.name = name
      self.species = species

   def __repr__(self):
      return f"{self.name} is a {self.species}"

   def make_sound(self, sound):
      print(f"this animal says {sound}")

class Dog(Animal):
   def __init__(self, name, breed):
      super().__init__(name, species="dog")
      self.breed = breed 

   def make_sound(self): #method overwriting
      return "Woof"


whiskers = Dog("Scout", "Beagle")
print(whiskers)
print(whiskers.make_sound())
print(whiskers.__dict__)
print(Dog.__mro__) # MRO is method resolution order, the order in which python looks for stuff - it's how you
#can do multiple inheritance