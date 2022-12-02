with open("input.txt", "r") as f:
    data: [str] = f.read().split("\n")


def convert(x: str) -> int:
    # rock
    if x in ['A', 'X']:
        return 1
    # paper
    if x in ['Y', 'B']:
        return 2
    # scissor
    if x in ['Z', 'C']:
        return 3


def get_loser(o: int) -> int:
    # rock
    if o == 1:
        # scissor
        return 3
    # paper
    if o == 2:
        # rock
        return 1
    # scissor
    if o == 3:
        # paper
        return 2


def get_draw(o: int) -> int:
    # rock
    if o == 1:
        return 1
    # paper
    if o == 2:
        return 2
    # scissor
    if o == 3:
        return 3


def get_winner(o: int) -> int:
    # rock
    if o == 1:
        # paper
        return 2
    # paper
    if o == 2:
        # scissor
        return 3
    # scissor
    if o == 3:
        # rock
        return 1


def get_result(x: [str]) -> [int, int]:
    # loose
    if x[1] == 1:
        loser = get_loser(x[0])
        return [loser, 0]

    # draw
    if x[1] == 2:
        draw = get_draw(x[0])
        return [draw, 3]

    # win
    if x[1] == 3:
        winner = get_winner(x[0])
        return [winner, 6]


result = 0
for d in data:
    s: [str] = d.split(' ')

    for b in get_result([convert(a) for a in s]):
        result += b

print(result)


