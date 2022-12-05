import re
import string

with open("input.txt", "r") as f:
    data: [str] = f.read().split("\n")


def get_char(pos) -> int:
    x = " 1   2   3   4   5   6   7   8   9"
    for index, char in enumerate(x):
        if char != '' and index == pos:
            return int(char) - 1


y = [[] for x in list(range(1, 10))]
z1 = y.copy()

for z in data[0:8]:
    for i, c in enumerate(z):
        if c in string.ascii_uppercase:
            y[get_char(i)].append(c)

for line in data[10:]:
    moves, from_, to = map(int, re.findall(r'[0-9]+', line))
    for _ in range(moves):
        y[to-1].insert(0, y[from_-1].pop(0))


print(''.join(map(str, [i[0] for i in y if len(i) > 0])))
