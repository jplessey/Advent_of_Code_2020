# --- Day 6: Custom Customs ---
from collections import Counter


# Part 1
yes_answers = 0
with open("input_6.txt") as input_file:
    for answers in input_file.read().split("\n\n"):
        yes_answers += len(set(answers.replace("\n", "")))

print(f"PART_1: {yes_answers}")


# Part 2
yes_answers = 0
with open("input_6.txt") as input_file:
    for group in input_file.read().split("\n\n"):
        group_count = len(group.split("\n"))
        for answer, count in Counter(answer for answer in group).items():
            if count == group_count:
                yes_answers += 1


print(f"PART_2: {yes_answers}")
