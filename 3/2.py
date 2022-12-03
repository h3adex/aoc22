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


def is_char_in_groups(item: str, groups: [str]) -> bool:
    for group in groups[0]:
        if item in group:
            for g in groups[1]:
                if item in g:
                    return True

    return False


elves = [data[x:x+3] for x in range(0, len(data), 3)]
result = 0
for groups in elves:
    for char in groups[0]:
        if is_char_in_groups(char, groups[-2:]):
            result += get_count(char)
            break

print(result)
