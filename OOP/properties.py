class Human:
   def __init__(self, name, age):
      self.name = name
      self._age = age

   @property  # getter
   def age(self):
      return self._age


   @age.setter #setter
   def age(self, value):
      self._age = value

bob = Human("Bob", 20)
print(bob.age) # invokes the getter method
bob.age = 40 # invokes the setter method
print(bob.age)
