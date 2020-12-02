# Find the two entries that sum to 2020; what do you get if you multiply them together?

import itertools
import time
from functools import reduce
from operator import mul

start_time = time.time()

f = open("/Users/caitlinhamilton/Programming/advent_of_code_2020/input_data/day_one.txt", "r")
data = [int(x) for x in f.read().splitlines()]
print(data)

def process_data(data):
    (x, y) = data
    return (x + y, x * y)

dict = {key: value for (key, value) in map(lambda xy : (xy[0] + xy[1], xy[0] * xy[1]), list(itertools.combinations(data, 2))) if key == 2020}
print(dict)
ans = dict.get(2020, None)
print("--- %s seconds ---" % (time.time() - start_time))
print(ans)



# Find the two entries that sum to 2020; what do you get if you multiply them together?

import itertools
import time

start_time = time.time()

f = open("/Users/caitlinhamilton/Programming/advent_of_code_2020/input_data/day_one.txt", "r")
data = [int(x) for x in f.read().splitlines()]

def process_data(data):
    (x, y, z) = data
    return x * y * z if x + y + z == 2020 else None

ans = list(filter(lambda x: x is not None, list(map(process_data, list(itertools.combinations(data, 3))))))[0]

print("--- %s seconds ---" % (time.time() - start_time))
print(ans)







