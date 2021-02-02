# --- Day 4: Passport Processing ---
import re


valid_passports = 0
final_valid_passports = 0
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


# PART 1
with open("input_4.txt") as input_file:
    for data in input_file.read().split("\n\n"):
        if all(field in data for field in required_fields):
            valid_passports += 1

print(f"PART_1: {valid_passports}")


# PART 2
HEX_COLOR = re.compile(r"[0-9a-f]")


def byr_valid(year):
    return 1920 <= int(year) <= 2002


def iyr_valid(year):
    return 2010 <= int(year) <= 2020


def eyr_valid(year):
    return 2020 <= int(year) <= 2030


def hgt_valid(height):
    if "cm" in height:
        return 150 <= int(height.replace("cm", "")) <= 193
    elif "in" in height:
        return 59 <= int(height.replace("in", "")) <= 76
    return False


def hcl_valid(hair_color):
    return "#" in hair_color and len(HEX_COLOR.findall(hair_color)) == 6


def ecl_valid(eye_color):
    return eye_color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid_valid(pass_id):
    return len(pass_id) == 9 and pass_id.isnumeric()


def cid_valid(cid):
    return True


passport_validation = {
    'byr': byr_valid,
    'iyr': iyr_valid,
    'eyr': eyr_valid,
    'hgt': hgt_valid,
    'hcl': hcl_valid,
    'ecl': ecl_valid,
    'pid': pid_valid,
    'cid': cid_valid
}


with open("input_4.txt") as input_file:
    for fields in input_file.read().split("\n\n"):
        fields = fields.replace("\n", " ").split(" ")
        fields = [field.split(":") for field in fields]
        fields = {field: data for field, data in fields}
        if all(field in fields.keys() for field in required_fields):
            validation = (
                passport_validation[field](fields[field])
                for field in fields
                )
            if all(validation):
                final_valid_passports += 1


print(f"PART_2: {final_valid_passports}")