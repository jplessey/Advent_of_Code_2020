# --- Day 11: Seating System ---
with open("input_11B.txt") as input_file:
    seats = [row.rstrip() for row in input_file]


#PART_1
def seat_checker_1(row_index, seat_index, all_seats):
    checker_list = []
    if row_index - 1 >= 0:
        checker_list.append((row_index - 1, [seat_index-1, seat_index, seat_index+1]))
    checker_list.append((row_index, [seat_index-1, seat_index+1]))
    if row_index + 1 <= len(all_seats) - 1:
        checker_list.append((row_index + 1, [seat_index-1, seat_index, seat_index+1]))
    occupied_seats = 0
    for row_index, indexes in checker_list:
        for index in indexes:
            if index >= 0 and index <= len(all_seats[row_index]) - 1:
                if all_seats[row_index][index] == "#":
                    occupied_seats += 1
    return occupied_seats


def boarding_ferry(all_seats, rules, tolerance):
    second_state =[]
    for _row_index, row in enumerate(all_seats):
        new_state = ""
        for _seat_index, seat in enumerate(row):
            if seat == ".":
                new_state += "."
                continue
            occupieds = rules(_row_index, _seat_index, all_seats)
            if seat == "L" and not occupieds:
                new_state += "#"
            elif seat == "#" and occupieds >= tolerance:
                new_state += "L"
            else:
                new_state += seat
        second_state.append(new_state)
    return second_state


new_state = boarding_ferry(seats, seat_checker_1, 4)
current_state = []
while current_state != new_state:
    current_state = new_state
    new_state = boarding_ferry(new_state,seat_checker_1,  4)
print("*******************")
print("PART_1")
print(sum(row.count("#") for row in current_state))
print("*******************")


#PART_2
def get_indexes(row_index, seat_index, _len=0, go_up=True):
    directions = []
    factor = 1
    _range = row_index if go_up else (_len - 1) - row_index
    for row in range(_range):
        moving_index = row_index - factor if go_up else row_index + factor
        left = seat_index - factor
        right = seat_index + factor
        center = seat_index
        directions.append((moving_index, [left, center, right]))
        factor += 1
    return directions


def get_directions(indexes_list, seats_list, rlimit=0):
    left_dir = center_dir = right_dir = ""
    for _row_index, indexes in indexes_list:
        left, center, right = indexes
        if left >= 0:
            left_dir += seats_list[_row_index][left]
        center_dir += seats_list[_row_index][center]
        if right <= rlimit - 1:
            right_dir += seats_list[_row_index][right]
    return left_dir, center_dir, right_dir


def is_occupied(direction):
    return direction.lstrip(".").startswith("#")


def seat_checker_2(row_index, seat_index, all_seats):
    rlimit = len(all_seats[row_index])
    _len = len(all_seats)
    all_directions = []
    # UP
    up_indexes = get_indexes(row_index, seat_index, _len=_len)
    up_directions = get_directions(up_indexes, all_seats, rlimit=rlimit)
    all_directions += up_directions
    # CENTER
    center_left = all_seats[row_index][0: seat_index][::-1]
    center_right = all_seats[row_index][seat_index + 1:rlimit]
    all_directions += (center_left, center_right)
    # DOWN
    down_indexes = get_indexes(row_index, seat_index, _len=_len, go_up=False)
    down_directions = get_directions(down_indexes, all_seats, rlimit=rlimit)
    all_directions += down_directions
    return sum(is_occupied(direction) for direction in all_directions if direction)


new_state = boarding_ferry(seats, seat_checker_2,  5)
current_state = []
while current_state != new_state:
    current_state = new_state
    new_state = boarding_ferry(new_state, seat_checker_2, 5)
print("*******************")
print("PART_2")
print(sum(row.count("#") for row in current_state))
print("*******************")
