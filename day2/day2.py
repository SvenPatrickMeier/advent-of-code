input_file_path = "./input.txt"

def is_valid_password(password: str):
    """
    Passwords always after pattern:
    /[0-9]{1}-[0-9]{1} [a-z]{1}: [a-z]*/g
    """
    print(password)
    splitted_password = password.split(" ")
    min, max = int(splitted_password[0].split("-")[0]), int(splitted_password[0].split("-")[1])
    req_char = splitted_password[1].strip(":")
    password = splitted_password[2]
   
    print(min, max, req_char, password)
    return password.count(req_char) >= min and password.count(req_char) <= max

def is_valid_toboggan_password(password: str):
    """
    Passwords always after pattern:
    /[0-9]{1}-[0-9]{1} [a-z]{1}: [a-z]*/g
    """
    splitted_password = password.split(" ")
    first, last = int(splitted_password[0].split("-")[0]), int(splitted_password[0].split("-")[1])
    req_char = splitted_password[1].strip(":")
    password = splitted_password[2]

    first_pw_index_is_letter = password[first-1] is req_char
    last_pw_index_is_letter = password[last-1] is req_char

    return (
        not (first_pw_index_is_letter and last_pw_index_is_letter) 
        and (
            first_pw_index_is_letter or last_pw_index_is_letter
        )
    )


with open(input_file_path, "r") as input:
    all_entries = list(map(lambda x: x, input.readlines()))
    input.close()

result = 0

# task for star one
for entry in all_entries:
    if is_valid_password(entry):
        result += 1
print(result)

# task for second star

result = 0

for entry in all_entries:
    if is_valid_toboggan_password(entry):
        result += 1
print(result)