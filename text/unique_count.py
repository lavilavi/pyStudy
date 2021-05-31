f = open('dealers', encoding='utf-8')
lns = f.readlines()

uniques = []

for ln in lns:
    if ln not in uniques:
        uniques.append(ln)
        print(uniques)
        print(len(uniques))
