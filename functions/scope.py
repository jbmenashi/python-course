total = 0

def increment():
    global total  #that's how you get a global variable to work as a local, but ONLY if you're change the variable
    total += 1
    return total

print(increment())

def outer():
    count = 0
    def inner():
        nonlocal count 
        count += 1
        return count 
    return inner()

# Documenting Functions
def doc():
    """This sets up a __doc__ key for your function"""
    print("whatever")