table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
xor = 177451812
add = 100618342136696320


def bv2av(bv: str):
    """Example: bv2av('17x411w7KC')
       Result:  170001"""

    index = []

    for each in bv:
        index.append(table.index(each))  # str.index()=str.find()

    numbers = [6, 2, 4, 8, 5, 9, 3, 7, 1, 0]

    for i in range(10):
        index[i] *= (58 ** numbers[i])

    av = sum(index) - add
    av = av ^ xor

    return av


def av2bv(av: int):
    """Example: av2bv(170001)
       Result:  '17x411w7KC'"""

    num = av ^ xor
    num += add

    values = []

    for n in range(10):
        values.append(num / 58**n) % 58)

    items = []

    for each in values:
        items.append(table[each])

    index = [9, 8, 1, 6, 2, 4, 0, 7, 3, 5]

    bv = [''] * 10

    for each in range(10):
        bv[index[each]] = items[each]

    return ''.join(bv)
