filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

vowels = ['a', 'e', 'i', 'o', 'u']
bad_strings = ['ab', 'cd', 'pq', 'xy']

nice = 0
naughty = 0

for line in input_lines:
    last_char = None
    vowel_count = 0
    found_double = False
    found_bad_string = False
    for c in line:
        if c in vowels:
            vowel_count += 1
        if last_char is not None:
            if last_char + c in bad_strings:
                found_bad_string = True
                break
            if last_char == c:
                found_double = True
        last_char = c

    if vowel_count >= 3 and found_double and not found_bad_string:
        nice += 1
    else:
        naughty += 1

print(nice)