table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
xor = 177451812
num = 100618342136696320


def bv2av(bv: str):
    """Example: 17x411w7KC"""

    index = []

    for each in bv:
        index.append(table.index(each))  # str.index()=str.find()

    numbers = [6, 2, 4, 8, 5, 9, 3, 7, 1, 0]

    for i in range(10):
        index[i] *= (58 ** numbers[i])

    av = sum(index) - sub
    av = av ^ xor

    return av
