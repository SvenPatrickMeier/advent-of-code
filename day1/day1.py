input_file_path = "./input.txt"
with open(input_file_path, "r") as input:
    all_entries = list(map(lambda x: int(x), input.readlines()))
    input.close()
print(all_entries)

result = 0

for tup_0 in all_entries:
    for tup_1 in all_entries:
        if tup_0 + tup_1 == 2020:
            result = tup_0 * tup_1
            break
print(result)