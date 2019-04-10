name = "Jacob" # this is not an iterator, BUT it is iterable

it_name = iter(name) # this is and actual iterator, which means you can do....

next(it_name) # "J"
next(it_name) # "A"
next(it_name) # "C"
next(it_name) # "O"
next(it_name) # "B"


def my_for_loop(iterable):
   iterator = iter(iterable)
   while True:
      try:
         print(next(iterator))
      except StopIteration:
         break



my_for_loop("hello")