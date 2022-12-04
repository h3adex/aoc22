with open("input.txt", "r") as f:
    data: [str] = f.read().split("\n")

count1 = 0

for line in data:
    e1, e2 = line.split(',')
    e1s, e1e = [int(x) for x in e1.split("-")]
    e2s, e2e = [int(x) for x in e2.split("-")]

    r1 = max(e1s, e2s)
    r2 = min(e1e, e2e)

    if r2 >= r1 == e1s and r2 == e1e or r1 == e2s and r2 == e2e:
        count1 += 1

print(count1)
