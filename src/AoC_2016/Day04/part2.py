import re
from functools import cmp_to_key

rooms_input = open("input.txt").read().splitlines()

pattern = re.compile("(.*)-([0-9]+)\\[(.*)\\]")
rooms_letter_counts = {}


class Room:

    def __init__(self, line):
        m = pattern.match(line)
        self.id = int(m.group(2))
        self.checksum = list(m.group(3))
        self.letter_counts = {}
        self.room_name_encrypted = m.group(1)

        for c in self.room_name_encrypted:
            if c != '-':
                self.letter_counts.setdefault(c, 0)
                self.letter_counts[c] += 1

        self.sorted_letters = list(self.letter_counts.items())
        self.sorted_letters.sort(key=cmp_to_key(lambda a, b: -1 if ((a[1] < b[1]) or (a[1] == b[1] and a[0] > b[0])) else 1), reverse=True)
        self.sorted_letters = list(map(lambda x: x[0], self.sorted_letters))

    def __repr__(self):
        decoded_name = ""
        for c in self.room_name_encrypted:
            decrypted_char = " "
            if c != '-':
                enc_char_int = ord(c) - ord('a')
                dec_char_int = (enc_char_int + self.id) % 26
                decrypted_char = chr(dec_char_int + ord('a'))
            decoded_name += decrypted_char
        return str(self.id) + ": " + decoded_name

    def is_valid(self) -> bool:
        valid = True

        for c in self.checksum:
            if c not in self.sorted_letters[:5]:
                valid = False
                break
        return valid


valid_room_sum = 0
rooms = []
for line in rooms_input:
    r = Room(line)
    if r.is_valid():
        rooms.append(r)
        valid_room_sum += r.id
        print(r)


# print(valid_room_sum)

