with open("input.txt", "r") as f:
    data: str = f.read().strip()


print(min([i + 4 for i, _ in enumerate(data) if len(set(data[i:i + 4])) == 4]))
print(min([i + 14 for i, _ in enumerate(data) if len(set(data[i:i + 14])) == 14]))
