# --- Day 2: Password Philosophy ---


def min_max_char(str):
    rg, char = str.split(" ")
    min, max = rg.split("-")
    return int(min), int(max), char


policies = []
valids_1, valids_2 = 0, 0
with open("input_2.txt") as input_file:
    for line in input_file:
        policy, password = line.rstrip().split(":")
        min, max, char = min_max_char(policy)
        # PART 1
        if min <= password.count(char) <= max:
            valids_1 += 1
        # PART 2
        if password.lstrip()[min-1] == char and password.lstrip()[max-1] != char:
            valids_2 += 1
        elif password.lstrip()[min - 1] != char and password.lstrip()[max - 1] == char:
            valids_2 += 1     

print(f"PART_1: {valids_1}")
print(f"PART_2: {valids_2}")
