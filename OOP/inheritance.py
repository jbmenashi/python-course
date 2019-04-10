class Animal:
   cool = True

   def make_sound(self, sound):
      print(f"this animal says {sound}")

class Cat(Animal):
   pass

whiskers = Cat()
whiskers.make_sound("Meow")
print(whiskers.cool) #true