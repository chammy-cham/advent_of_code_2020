#How many passwords are valid according to their policies?
from collections import Counter
import time
from functools import reduce
from operator import mul

start_time = time.time()

f = open("/Users/caitlinhamilton/Programming/advent_of_code_2020/input_data/day_two.txt", "r")

def process_data(data_entry):
    data_entry = data_entry.split(" ")
    c = Counter(data_entry[2])
    if int(data_entry[0].split("-")[0]) <= c.get(data_entry[1].strip(":"), 0) <= int(data_entry[0].split("-")[1]):
        return True
    else:
        return False

print(sum([process_data(x) for x in f.read().splitlines()]))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

f = open("/Users/caitlinhamilton/Programming/advent_of_code_2020/input_data/day_two.txt", "r")
def process_data_part_two(data_entry):
    data_entry = data_entry.split(" ")
    position_1 = int(data_entry[0].split("-")[0]) - 1
    position_2 = int(data_entry[0].split("-")[1]) - 1
    letter = data_entry[1].strip(":")
    pw = list(data_entry[2])
    if pw[position_1] == letter and pw[position_2] == letter or pw[position_1] != letter and pw[position_2] != letter:
        return False
    else:
        return True

print(sum([process_data_part_two(x) for x in f.read().splitlines()]))
print("--- %s seconds ---" % (time.time() - start_time))