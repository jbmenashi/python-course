first_zip = zip([1,2,3], [4,5,6])

list(first_zip) # [(1, 4), (2, 5), (3, 6)]
dict(first_zip) # {1: 4, 2: 5, 3: 6}

# Once you zip it, you have to turn it into a list or a dictionary to see it
# If it's different lengths, it STOPS at the shortest iterable
# You can do as many different iterators as you want

midterms = [80, 78, 94]
finals = [90, 77, 91]
students = ["bob", "tim", "jasper"]

# how do we get {"bob": 90, "tim": 78, "jasper": 94}

{group[0]: max(group[1], group[2]) for group in zip(students, midterms, finals)}

dict(zip(students, map(lambda pair: max(pair), zip(midterms, finals))))


def interleave(str1, str2):
   #  zipped_tuples = list(zip(str1, str2))
   #  something = ["".join(tup) for tup in zipped_tuples]
   #  print("".join(something))

   return "".join(["".join(tup) for tup in list(zip(str1, str2))])

interleave("hi", "no")


