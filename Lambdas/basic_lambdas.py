# lambdas are essentially anonymous functions

def square(num):
   return num * num

# is the same as

lambda num: num * num 
# has to be a single line, a single expression, and you don't need a return keyword

# Map function
nums = [2, 4, 6, 8, 10]
doubles = map(lambda num: num * 2, nums) #it looks like a callback, so yeah it it's essentially one
print(list(doubles))


def decrement_list(nums):
    return list(map(lambda num: num - 1, nums))

# Filter function, it's just like JS but lambda version

more_nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda num: num % 2 == 0, more_nums)) # [2, 4]

# Filter AND map


def triple_and_filter(nums):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, nums)))

names = ["Bob", "Jim", "Landry"]
result = list(map(lambda name: f"Hello {name}", filter(lambda name: len(name) < 5, names)))
print(result)

# What's dumb is you can just do a list comp
better_result = [f"Hello {name}" for name in names if len(name) < 5]
print(better_result)


def extract_full_name(names):
    list_of_names = []
    for item in names:
        full_name = ""
        for val in item.values():
            full_name += val + " "
        list_of_names.append(full_name[:-1])
    return list_of_names


def extract_full_names(names):
    return list(map(lambda val: f"{val['first']} {val['last']}", names))
