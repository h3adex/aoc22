with open("input.txt", "r") as f:
    data: [str] = f.read().split("\n\n")

top_elve = sorted([sum([int(y) for y in x.split("\n") if len(y) > 0]) for x in data])[-1]
print(top_elve)
top_three = sum(sorted([sum([int(y) for y in x.split("\n") if len(y) > 0]) for x in data])[-3:])
print(top_three)
