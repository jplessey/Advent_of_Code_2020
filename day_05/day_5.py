# --- Day 5: Binary Boarding ---


def find_position(code, lower_limit=0, upper_limit=127):
    for letter in code:
        if letter == "F" or letter == "L":
            upper_limit = (upper_limit - lower_limit) // 2 + lower_limit
        elif letter == "B" or letter == "R":
            lower_limit = upper_limit - (upper_limit - lower_limit) // 2
    return lower_limit  # lower_limit will be equal to upper_limit


def find_seat(code):
    return find_position(code[:8]), find_position(code[7:], upper_limit=7)


all_seats = {}
with open("input_5.txt") as input_file:
    for boarding_code in input_file.readlines():
        row, column = find_seat(boarding_code.rstrip())
        seat = all_seats.setdefault(row, [])
        seat.append(column)

# PART 1
highest_row = sorted(all_seats.keys()).pop()
print(f"PART_1: {highest_row * 8 + all_seats[highest_row][-1]}")

# PART 2
# Finding the missing seat id
row, columns = min(sorted(all_seats.items())[1:-1], key=lambda t:len(t[1]))
missing_column = (column for column in range(7) if column not in columns)
print(f"PART_2: {row * 8 + next(missing_column)}")
