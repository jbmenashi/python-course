class Pet:
   allowed = ['cat', 'dog ']
   def __init__(self, name, species):
      if species not in self.allowed:
         raise ValueError("illegal pet")
      self.name = name
      self.species = species 


cat = Pet("Blue", "cat")
dog = Pet("Ruff", "dog")