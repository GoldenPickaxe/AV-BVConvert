table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'


def bv2av(bv: str):
    """Example: 17x411w7KC"""

    index = []

    for each in bv:
        index.append(table.index(each))  # str.index()=str.find()

    numbers = [6, 2, 4, 8, 5, 9, 3, 7, 1, 0]

    for i in range(10):
        index[i] *= (58 ** numbers[i])

    av = sum(index) - 100618342136696320
    av = av ^ 177451812

    return av
