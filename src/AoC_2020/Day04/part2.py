import functools
import re


def year_validation(value, low, high):
    m = re.match("^([0-9]{4})$", value)
    if m:
        return low <= int(m.group(1)) <= high
    else:
        return False


def byr(value):
    return year_validation(value, 1920, 2002)


def iyr(value):
    return year_validation(value, 2010, 2020)


def eyr(value):
    return year_validation(value, 2020, 2030)


def hgt(value):
    m = re.match("^([0-9]*)(cm|in)$", value)
    if m:
        low = 150 if (m.group(2) == 'cm') else 59
        high = 193 if (m.group(2) == 'cm') else 76
        return low <= int(m.group(1)) <= high
    else:
        return False


def hcl(value):
    return re.match("^#[0-9a-f]{6}$", value) is not None


def ecl(value):
    return re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", value) is not None


def pid(value):
    return re.match("^[0-9]{9}$", value) is not None


filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

pattern = re.compile("(byr|iyr|eyr|hgt|hcl|ecl|pid):([^ ]*)")

buffer = ""
valid_count = 0

for line in input_lines:
    if len(line) > 0:
        buffer = buffer + " " + line
    else:
        fields = pattern.findall(buffer)
        if len(fields) == 7:
            map_fields = dict((m[0], m[1]) for m in fields)

            valid = functools.reduce(lambda a, b: a and b, map(lambda x: eval(x)(map_fields[x]), map_fields), True)
            if valid:
                valid_count += 1
        buffer = ""

print(buffer)
print(valid_count)
