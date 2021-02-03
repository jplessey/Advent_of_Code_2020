# --- Day 13: Shuttle Search ---
import re


BUS_ID_RE = re.compile(r"\d+")
with open("input_13.txt") as input_file:
    data = iter(input_file.readlines())
    est_timestamp = int(next(data).rstrip())
    buses_data = next(data).rstrip()
    all_buses = buses_data.split(",")
    ids = BUS_ID_RE.findall(buses_data)

# PART_1
bus_timestamps = {
    id: (0, int(id), int(id)*2, int(id)*3)
    for id in ids
}

is_this_my_bus = {}
tm = 0
for id in bus_timestamps.keys():
    trip = int(id)
    while tm < est_timestamp:
        tm += trip
    is_this_my_bus[id] = tm
    tm = 0

i_board = min(is_this_my_bus.values())
for id, arrive in is_this_my_bus.items():
    if arrive == i_board:
        print(f"PART 1: {(arrive - est_timestamp) * int(id)}")
        break
