class Chicken:
   total_eggs = 0 #class variable

   def __init__(self, name):
      self.name = name
      self.eggs = 0 #instance attribute

   def lay_egg(self):
      Chicken.total_eggs += 1 #adjust class variable
      self.eggs += 1 #adjust instance attribute
      return self.eggs

   @classmethod
   def display_total_eggs(cls):
      return cls.total_eggs



