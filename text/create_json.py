values = [line.rstrip() for line in open('hierarchy')]
print(values)

json = "{"
for value in values:
    if value.startswith("\""):
        json += "\"" + value + "\":"

