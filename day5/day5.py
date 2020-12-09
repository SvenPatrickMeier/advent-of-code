input_file_path = "./input.txt"
import re
from functools import reduce

with open(input_file_path, "r") as input:
    lines = list(map(lambda x: x, input.readlines()))
    input.close()

def parse_to_binary(boarding_pass: str):
    return "".join(list(map(lambda x: "0" if x in "FL" else "1", boarding_pass)))

def get_highest_seat_id(boarding_passes: list):
    binaries = list(map(lambda x: parse_to_binary(x), boarding_passes))
    passes = list(
        map(
            lambda binary: ((int(binary[0:7], 2) * 8 + (int(binary[7:-1], 2)))),
            binaries))
    return reduce(lambda acc, x: x if x > acc else acc, passes)

def get_highest_seat_id_super(boarding_passes: list):
    return reduce(
        lambda acc, x: x if x > acc else acc,
        list(map(
            lambda binary: ((int(binary[0:7], 2) * 8 + (int(binary[7:-1], 2)))),
            list(map(lambda x: "".join(list(map(lambda x: "0" if x in "FL" else "1", x))),
                boarding_passes))))
    )

print(get_highest_seat_id(lines))
print(get_highest_seat_id_super(lines))