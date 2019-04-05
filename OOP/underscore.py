class User:
   def __init__(self, name):
      self.name = name 

      self._private = "This is a private method"
      self.__instance = "This is an instance method - only applies to this class"