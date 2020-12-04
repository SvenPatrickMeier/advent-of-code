from functools import reduce

### READ INPUT
input_file_path = "./input.txt"
with open(input_file_path, "r") as input:
    all_entries = list(map(lambda x: x.replace("\n", ""), input.readlines()))
    input.close()
entry_length = len(all_entries[0])

def position_is_tree(landscape: str, coord: int):
    return True if landscape[coord] == "#" else False

def sum_positions(entries: list, line_length: int, _x: int = 1, _y: int = 1):
    result = 0
    x, y = _x, _y
    while True:
        if y >= len(all_entries):
            break
        elif position_is_tree(all_entries[y], x % entry_length):
            result += 1
        x += _x
        y += _y
    return result

def multiply_positions(tree_sums: list):
    return reduce((lambda x, y: x * y), tree_sums)

# star one solution
star_one_result = sum_positions(all_entries, entry_length, 3, 1)
print(f'Star one solution: {star_one_result}')

# star two solution
patterns = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

star_two_result = multiply_positions(
    map(lambda x: sum_positions(all_entries, entry_length, x[0], x[1]), patterns)
)

print(f'Star two solution: {star_two_result}')
