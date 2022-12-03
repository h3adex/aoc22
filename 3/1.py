import string

with open("input.txt", "r") as f:
    data: [str] = f.read().split("\n")


def get_count(item: str) -> int:
    for index, x in enumerate(list(string.ascii_lowercase)):
        if item == x:
            return index + 1

    for index, x in enumerate(list(string.ascii_uppercase)):
        if item == x:
            return index + 27

    return 0


result = 0
for line in data:
    part1, part2 = line[:len(line)//2], line[len(line)//2:]

    matched_char = []
    for character in part1:
        if character in part2 and character not in matched_char:
            result += get_count(character)
            matched_char.append(character)

print(result)
