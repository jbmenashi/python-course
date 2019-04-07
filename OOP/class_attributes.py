class User:
   active_users = 0

   def __init__(self, first, last, age):
      self.first = first
      self.last = last
      self.age = age
      User.active_users += 1

   def full_name(self):
      return f"{self.first} {self.last}"

   def initials(self):
      return f"{self.first[0]}.{self.last[0]}"

   