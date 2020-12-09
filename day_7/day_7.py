# --- Day 7: Handy Haversacks ---
import re


INNER_COLORS = re.compile(r"([0-9]) (\w+ \w+) bag")
OUTER_COLOR = re.compile(r"(\w+ \w+) bags contain")
colors_nodes_rules = {}
with open("input_7.txt") as input_file:
    for line in input_file:
        outer_color = OUTER_COLOR.match(line).group(1)
        colors_nodes_rules[outer_color] = {
            color: int(number) 
            for number, color in INNER_COLORS.findall(line)
        }


# PART_1
color = {}
for node in colors_nodes_rules.keys():
    color[node] = "W"


# Shout Out to PyTech Vision video on DFS and Graph Data Structure
# which helped me ifgure out how to create the traversal connections
# https://www.youtube.com/watch?v=FvGCzzfdOLw&list=LL&index=6&t=321s
def dfs_util(u):
    color[u] = "G"
    dfs_traversal_output.append(u)
    for v in colors_nodes_rules[u].keys():
        if color[v] == "W":
            dfs_util(v)
    color[u] = "B"


color_to_find = "shiny gold"
count = 0
dfs_traversal_output = []
for _color in colors_nodes_rules:
    dfs_util(_color)
    if _color != color_to_find and color_to_find in dfs_traversal_output:
        count += 1
    for node in colors_nodes_rules.keys():
        color[node] = "W"
    dfs_traversal_output = []

print(f"PART_1: {count}")


# PART_2
def bags_inside(color, tree):
    count = 0
    if tree[color]:
        for inner_color, bags_num in tree[color].items():
            count += bags_num + bags_num * bags_inside(inner_color, tree)
    else:
         return 0
    return count

print(f"PART_2: {bags_inside('shiny gold', colors_nodes_rules)}")