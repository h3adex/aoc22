with open("input.txt", "r") as f:
    data: [str] = f.read().split("\n")


def convert(x: str) -> int:
    if x in ['A', 'X']:
        return 1
    if x in ['Y', 'B']:
        return 2
    if x in ['Z', 'C']:
        return 3


def get_result(x: [str]) -> int:
    if x[0] == x[1]:
        return 3
    if (x[0] == 1 and x[1] == 2) or (x[0] == 2 and x[1] == 3) or (x[0] == 3 and x[1] == 1):
        return 6
    return 0


result = 0
for d in data:
    s: [str] = d.split(' ')
    result += get_result([convert(a) for a in s]) + convert(s[1])

print(result)


