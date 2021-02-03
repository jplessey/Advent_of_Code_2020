# --- Day 3: Toboggan Trajectory ---


def how_many_trees(right=1, down=1):
    index, count = 0, 0
    down_checker = 1
    with open("input_3.txt") as input_file:
        for id, row in enumerate(input_file.readlines(), start=1):
            if id == down_checker:    
                row = row.rstrip()
                if row[index] == "#":
                    count += 1
                if index + right >= 30:
                    index = (right - 1) - (30 - index)
                else:
                    index += right
                down_checker = id + down    
            else:
                continue
    return count        


# PART 1
print(f"PART_1: {how_many_trees(3, 1)}")


# PART 2
slope_a = how_many_trees(1, 1)
slope_b = how_many_trees(3, 1)
slope_c = how_many_trees(5, 1)
slope_d = how_many_trees(7, 1)
slope_e = how_many_trees(1, 2)

print(f"PART_2: {slope_a * slope_b * slope_c * slope_d *slope_e}")


