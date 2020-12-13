# --- Day 12: Rain Risk ---
import re
from dataclasses import dataclass


@dataclass
class Ship:
    w_e_pos: str = "E"
    w_e_value: int = 0
    n_s_pos: str = "N"
    n_s_value: int = 0
    facing: str = "E"
    way_point_A = "E"
    way_point_A_value = 10
    way_point_B = "N"
    way_point_B_value = 1
    pairs = {"N": "S", "S": "N", "E": "W", "W": "E"}

    def __repr__(self):
        return f"{self.w_e_pos} {self.w_e_value}, {self.n_s_pos} {self.n_s_value}"

    def calc_pos(self, action, value):
        if action in ("N", "S"):
            if self.n_s_pos == action:
                self.n_s_value += value
            elif self.n_s_pos == self.pairs[action]:
                if self.n_s_value - value <= 0:
                    self.n_s_value = abs(self.n_s_value - value)
                    self.n_s_pos = action
                else:
                    self.n_s_value = self.n_s_value - value
        else:
            if self.w_e_pos == action:
                self.w_e_value += value
            elif self.w_e_pos == self.pairs[action]:
                if self.w_e_value - value <= 0:
                    self.w_e_value = abs(self.w_e_value - value)
                    self.w_e_pos = action
                else:
                    self.w_e_value = self.w_e_value - value

    @property
    def waypoints(self):
        return ((self.way_point_A, self.way_point_A_value),
                (self.way_point_B, self.way_point_B_value))

    def man_distance(self):
        return self.n_s_value + self.w_e_value


def str_to_num(tup):
    act, val = tup
    return act, int(val)


ACTION_VALUE_RE = re.compile(r"([A-Z])(\d+)")
with open("input_12.txt") as input_file:
    navigation = [
        str_to_num(ACTION_VALUE_RE.match(line).groups())
        for line in input_file
        ]

# PART_1
ship = Ship()
for action, value in navigation:
    if action == "F":
        action = ship.facing
    if action == "R" or action == "L":
        pos = ["N", "E", "S", "W", "N", "E", "S", "W"]
        if action == "L":
            pos = list(reversed(pos))
        shift = value/90
        new_facing = int(pos.index(ship.facing) + shift)
        ship.facing = pos[new_facing]
    else:
        ship.calc_pos(action, value)


print("*******************")
print(f"PART_1: {ship.man_distance()}")
print("*******************")


# PART_2
ship = Ship()
for action, value in navigation:
    if action == "F":
        for _action, _value in ship.waypoints:
            ship.calc_pos(_action, _value*value)
    elif action in ("N", "S", "W", "E"):
        if action == ship.way_point_A:
            ship.way_point_A_value += value
        elif action == ship.way_point_B:
            ship.way_point_B_value += value
        else:
            _key = ship.pairs[action]
            if _key == ship.way_point_A:
                if ship.way_point_A_value - value < 0:
                    ship.way_point_A_value = abs(ship.way_point_A_value - value)
                    ship.way_point_A = action
                else:
                    ship.way_point_A_value -= value
            elif _key == ship.way_point_B:
                if ship.way_point_B_value - value < 0:
                    ship.way_point_B_value = abs(ship.way_point_B_value - value)
                    ship.way_point_B = action
                else:
                    ship.way_point_B_value -= value
    elif action == "R" or action == "L":
        target = (ship.way_point_A, ship.way_point_B)
        rot_1 = [("E", "N"), ("S", "E"), ("W", "S"), ("N", "W"), ("E", "N"), ("S", "E"), ("W", "S")]
        rot_2 = [("E", "S"), ("S", "W"), ("W", "N"), ("N", "E"), ("E", "S"), ("S", "W"), ("W", "N")]
        pos = rot_1
        if target in rot_2:
            pos = rot_2
        if action == "L":
            pos = list(reversed(pos))
        shift = value/90
        new_wp = int(pos.index(target) + shift)
        ship.way_point_A, ship.way_point_B = pos[new_wp]


print("*******************")
print(f"PART_2: {ship.man_distance()}")
print("*******************")