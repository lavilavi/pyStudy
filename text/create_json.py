values = [line.rstrip() for line in open('hierarchy')]
print(values)


def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


json = "{"
for value in values:
    if value != "":
        splitted = value.split(":")
        json = json + "\"" + splitted[0]
        print(splitted[1])
        print(is_num(splitted[1]))
        if not is_num(splitted[1]):
            json = json + "\":\"" + value.split(":")[1] + "\","
        else:
            json = json + "\":" + value.split(":")[1] + ","
json = json[:len(json) - 1] + "}"
print(json)
