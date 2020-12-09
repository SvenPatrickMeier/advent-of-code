input_file_path = "./input.txt"
import re
with open(input_file_path, "r") as input:
    lines = list(map(lambda x: x, input.readlines()))
    input.close()

def is_passport_data_end(line: str):
    return line == "\n"

def add_to_passport_data(index: int, line: str, passports: list):
    if index < len(passports):
        passports[index].append(line)
    else:
        passports.insert(index, [line])
    return passports

def parse_input_to_passport_data(input: list):
    passports = []
    counter = 0
    for line in input:
        if is_passport_data_end(line):
            counter += 1
        else:
            passports = add_to_passport_data(counter, line, passports)
    return list(map(lambda x: " ".join(x).replace("\n", ""), passports))

def is_digit_number(digits: int, test_number: int):
    return True if len(str(test_number)) == digits else False

def is_valid_byr(byr: int):
    pattern = re.compile(r'^[\d]{4}')
    if not pattern.match(str(byr)):
        return False
    else:
        return byr < 2003 and byr > 1919

def is_valid_iyr(iyr: int):
    pattern = re.compile(r'^[\d]{4}')
    if not pattern.match(str(iyr)):
        return False
    else:
        return iyr < 2020 and iyr > 2010

def is_valid_eyr(eyr: int):
    pattern = re.compile(r'^[\d]{4}')
    if not pattern.match(str(eyr)):
        return False
    else:
        return eyr < 2020 and eyr > 2010

def is_valid_passport_property(property_string: str):
    split_prop = property_string.split(":")
    prop_key, value = split_prop[0], split_prop[1]
    print(prop_key, value)
    if (prop_key == "cid"):
            return True
    if prop_key == "byr":
        value = int(value)
        return is_valid_byr(value)
    elif prop_key == "iyr":
        value = int(value)
        return is_valid_iyr(value)
    elif prop_key == "eyr":
        value = int(value)
        return is_valid_eyr(value)
    elif prop_key == "hgt":
        if value.endswith("cm"):
            value = int(value.replace("cm", ""))
            return value >= 150 and value <= 193
        elif value.endswith("in"):
            value = int(value.replace("in", ""))
            return value >= 56 and value <= 76
    elif prop_key == "hcl":
        pattern = re.compile(r'(^#[0-9a-f]{6}$)')
        return bool(pattern.match(value))
    elif prop_key == "ecl":
        pattern = re.compile(r'([amb|blu|brn|gry|grn|hzl|oth]{1})')
        return bool(pattern.match(value))
    elif prop_key == "pid":
        pattern = re.compile(r'^[\d]{9}')
        return bool(pattern.match(value))
    # elif prop_key == "cid":
    #     return True

def passport_matches_conditions(passport: str):
    # if not (passport.count(":") == 7 and "cid" not in passport):
    #     return False
    # else:
    # if passport.count(":") < 7:
    #     return False
    pairs = passport.count(":")
    if pairs < 8 and "cid" not in passport:
        return list(map(lambda x: is_valid_passport_property(x), passport.split(" "))).count(False) == 0
   


def is_valid_passport(passport: str):
    return passport_matches_conditions(passport)    


### Actual solution for the day 4 puzzle
passports = parse_input_to_passport_data(lines)
print(passports[0])

# First star solution
print(f'CALL ME GOD IF THIS WORKS, THIS IS THE MF SOLUTION: {list(map((lambda x: 1 if is_valid_passport(x) else -1), passports)).count(1)}')

print(f'OMG I am so good: {list(map((lambda x: 1 if is_valid_passport(x) else -1), passports)).count(1)}')