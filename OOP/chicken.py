class Chicken:
   total_eggs = 0 #class variable

   def __init__(self, species, name):
      self.species = species
      self.name = name
      self.eggs = 0 #instance attribute

   def lay_egg(self):
      Chicken.total_eggs += 1 #adjust class variable
      self.eggs += 1 #adjust instance attribute
      return self.eggs

   @classmethod
   def display_total_eggs(cls): # stands for class
      return cls.total_eggs # because of the class method decorator, the self is now the class

   @classmethod
   def from_string(cls, str):   
      name,species = str.split(",")
      return cls(name, species)
