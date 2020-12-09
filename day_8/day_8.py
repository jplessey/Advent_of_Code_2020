# --- Day 8: Handheld Halting ---
from dataclasses import dataclass


@dataclass
class Instruction:
    name: str
    sign: str
    value: int
    executed: bool = False


instructions = []
with open("input_8.txt") as input_file:
    for line in input_file:
        name, raw_instruction = line.rstrip().split(" ")
        sign = raw_instruction[0]
        value = int(raw_instruction[1:])
        instructions.append(Instruction(name=name, sign=sign, value=value))

# PART_1

index = 0
accumulator = 0
possible_bugs = []
while True:
    action = instructions[index]
    if action.executed:
        print("***********************")
        print(f"PART_1 Accumulator: {accumulator}")
        print("Out of the loop...")
        print("***********************")
        break
    if action.name == "nop":
        possible_bugs.append((index, "nop"))
        index += 1
        action.executed = True
    elif action.name == "acc":
        if action.sign == "+":
            accumulator += action.value
        else:
            accumulator -= action.value
        index += 1
        action.executed = True
    elif action.name == "jmp":
        possible_bugs.append((index, "jmp"))
        if action.sign == "+":
            index += action.value
        else:
            index -= action.value

# PART_2

for _index, _ in possible_bugs:
    index = 0
    accumulator = 0
    for instruction in instructions:
        instruction.executed = False
    while True:
        if index == len(instructions):
            print(f"PART_2 Accumulator: {accumulator}")            
            print("Execution complete...")
            print(f"Bug at index: {_index}")
            print("***********************")
            break
        action = instructions[index]
        if action.executed:
            break
        name, sign, value = action.name, action.sign, action.value
        if _index == index:
            if name == "jmp":
                name = "nop"
            else:
                name = "jmp"
        if name == "nop":
            index += 1
            action.executed = True
        elif name == "acc":
            if sign == "+":
                accumulator += value
            else:
                accumulator -= value
            index += 1
            action.executed = True
        elif name == "jmp":
            if sign == "+":
                index += value
            else:
                index -= value
