def sum_all_nums(*args): # args becomes a tuple
   total = 0
   for num in args:
      total += num
   return total

def check_names(*args):
   if "Jacob" in args:
      return "That's me"
   else:
      return "Not Me"

# because it creates a tuple, if you put a list in as your arg, it won't separate out every value
# so just put a star in front

nums = (1, 2, 3, 4, 5, 6)
sum_all_nums(*nums)

def fav_colors(**kwargs): # stands for keyword args, so like Jacob=person, kwargs becomes a dictionary
   for key, value in kwargs.items(): #so you have to iterare through like a dictionary
      print(key, value)


def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word


# dictionary unpacking is kind of the same thing
def display_names(first, second):
   print(f"{first} says hello to {second}")

names = {"first": "Jacob", "second": "Menashi"}
display_names(**names)