# --- Day 9: Encoding Error ---
from itertools import permutations


def sub_suma(size, index, sequence):
    assert index - size >= 0, "Index smaller than size."
    return set(
        a + b
        for a, b in
        permutations(sequence[index - size:index], 2)
    )


with open("input_9.txt") as input_file:
    numbers = [int(num) for num in input_file]
    for _index, number in enumerate(numbers):
        try:
            if number not in sub_suma(25, _index, numbers):
                invalid_number = number
                break
        except AssertionError:
            continue
print(f"PART_1: {invalid_number}")


def progresive_sum(target, sequence):
    range = 2
    index = 0
    while True:
        if index + range > len(sequence) - 1:
            range += 1
            index = 0
        elif sum(sequence[index: index + range]) == target:
            return sequence[index: index + range]
        else:    
            index += 1


smallest, *_,  largest = sorted(progresive_sum(invalid_number, numbers))
print(f"PART_2: {smallest + largest}")
