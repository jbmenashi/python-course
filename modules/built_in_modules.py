# There's lots of built-in modules

import random as randooo # you can alias any module

randooo.choice(["A", "B", "C"])

# but you don't really need to import everything

from random import randint # you can import specific things
from random import * # this still imports everything BUT now you don't need random. before functions
randint(1, 100)



