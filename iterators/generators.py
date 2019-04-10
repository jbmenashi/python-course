# A quick way of creating iterators
# its the yield thing

def count_up_to(max):
   count = 1
   while count <= max:
      yield count
      count += 1

count_up_to(5) # returns a generator object

counter = count_up_to(5)
next(counter) #1


def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)
