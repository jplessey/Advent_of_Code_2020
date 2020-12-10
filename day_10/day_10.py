# --- Day 10: Adapter Array ---
from itertools import zip_longest
import math


with open("input_10.txt") as input_file:
    adapters = [int(num) for num in input_file]

# PART_1
adapters = adapters + [0, max(adapters)+3]
adapters.sort()
diffs = [b - a for a, b in zip(adapters, adapters[1:])]
print(f"PART_1: {diffs.count(1) * diffs.count(3)}")

# PART_2
# Find all subsequences of 1 in diffs, e.g: [1, 1] - [1, 1, 1] - [1, 1, 1, 1]
all_one_sequences = []
one_sequence = []
for value, next in zip_longest(diffs, diffs[1:], fillvalue=None):
    if value == 1 and next == 1:
        one_sequence.append(value)
    elif one_sequence and value == 1:
        one_sequence.append(value)
    elif one_sequence and value != 1:
        all_one_sequences.append(one_sequence)
        one_sequence = []

# The max length of subsequences of 1 was 4
multipliers = {
    2: 2,  # [1, 1] ---> [1, 1] - [2]
    3: 4,  # [1, 1, 1] ---> [1, 1, 1] - [2, 1] - [1, 2] - [3]
    4: 7   # [1, 1, 1, 1] ---> [1, 1, 1, 1] - [1, 2, 1] - [2, 1, 1] - [1, 1, 2] - [3, 1] - [1, 3] - [2, 2]
               }

print(f"PART_2: {math.prod(multipliers[len(seq)] for seq in all_one_sequences)}")
