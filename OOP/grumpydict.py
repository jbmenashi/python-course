class GrumpyDict(dict):
   def __repr__(self): # don't need an init because you're inheriting from dict
      print("BOOOOOOO")
      return super().__repr__()

   def __missing__(self, key):
      print(f"{key} aint here fam")

data = GrumpyDict({"city": "Boston", "state": "Mass"})
print(data)
data['eee']