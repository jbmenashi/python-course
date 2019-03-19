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

def fav_colors(**kwargs): # stands for keyword args, so like Jacob=person, kwargs becomes a dictionary
   for key, value in kwargs.items(): #so you have to iterare through like a dictionary
      print(key, value)


def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word
