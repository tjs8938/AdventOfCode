import re
from typing import List

# inputs = open("test1.txt").read().splitlines()
inputs = open("input.txt").read().splitlines()


def supports_tls(line: str) -> bool:
    inside_brackets = False
    has_abba = False
    char_buffer = ""

    for c in line:

        if c == '[':
            inside_brackets = True
            char_buffer = ""
        elif c == ']':
            inside_brackets = False
            char_buffer = ""
        elif len(char_buffer) == 0:
            char_buffer += c
        elif len(char_buffer) == 1:
            if c == char_buffer:
                char_buffer = c
            else:
                char_buffer += c
        elif len(char_buffer) == 2:
            if c != char_buffer[1]:
                char_buffer = char_buffer[1] + c
            else:
                char_buffer += c
        else:
            if c != char_buffer[0]:
                if c == char_buffer[2]:
                    char_buffer = c
                else:
                    char_buffer = char_buffer[2] + c
            else:
                char_buffer = ""
                if inside_brackets:
                    return False
                else:
                    has_abba = True
    return has_abba


def find_string(string: str, substring: str):
    try:
        return string.index(substring)
    except ValueError:
        return -1


def supports_ssl(line):
    pattern = re.compile("(.*?)(\\[.*?\\]|$)")
    bab_list: List[str] = []
    match_groups = pattern.findall(line)
    for m in match_groups:
        aba = m[0]
        for i in range(len(aba) - 2):
            if aba[i] == aba[i + 2] and aba[i] != aba[i + 1]:
                bab_list.append(aba[i + 1] + aba[i] + aba[i + 1])
    for m in match_groups:
        inside: str = m[1]
        for bab in bab_list:
            if find_string(inside, bab) >= 0:
                return True
    return False


support_tls = 0
for line in inputs:
    if supports_tls(line):
        support_tls += 1

print(support_tls)


# inputs = open("test2.txt").read().splitlines()

support_ssl = 0
for line in inputs:
    if supports_ssl(line):
        support_ssl += 1

print(support_ssl)
