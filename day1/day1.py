input_file_path = "./input.txt"
with open(input_file_path, "r") as input:
    all_entries = list(map(lambda x: int(x), input.readlines()))
    input.close()

result = 0

# Task for star one
for tup_0 in all_entries:
    for tup_1 in all_entries:
        if tup_0 + tup_1 == 2020:
            result = tup_0 * tup_1
            break

# Task for two stars
for tup_0 in all_entries:
    for tup_1 in all_entries:
        for tup_2 in all_entries:
            if tup_0 + tup_1 + tup_2 == 2020:
                result = tup_0 * tup_1 * tup_2
                break
print(result)