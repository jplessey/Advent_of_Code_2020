# --- Day 1: Report Repair ---
from itertools import combinations


with open("input_1.txt") as input_file:
    entries = [int(entry) for entry in input_file.read().split("\n")]
    # PART 1
    for entry_a, entry_b in combinations(entries, 2):
        if entry_a + entry_b == 2020:
            print(f"PART_1: {entry_a * entry_b}")
            break
    # PART 2   
    for entry_a, entry_b, entry_c in combinations(entries, 3):
        if entry_a + entry_b + entry_c == 2020:
            print(f"PART_2: {entry_a * entry_b * entry_c}")
            break
