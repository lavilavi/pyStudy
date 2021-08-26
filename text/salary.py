base = 309300
zangyo = 20
house = 0
social = 15000 + 45000
residential = 326000 / 12
income = 15000
tax = residential + income
trans = 16900/3


def zangyo_dai():
    return (base + 8000) * (1 / 163 * 1.3 * zangyo)


def monthly():
    return base + 8000 + house + zangyo_dai() + trans


def bonus():
    return base * 6


def total():
    return monthly() * 12 + bonus()


def first_year():
    return monthly() * 12 + bonus() / 12 * 7


def tedori_month():
    return monthly() - social - tax


def total_tedori():
    return total() * 0.8


if __name__ == '__main__':
    print(total())
