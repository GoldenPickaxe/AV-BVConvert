table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
def bv2av(bv:str):
    av = []
    for each in bv:
        av.append(table.find(each))
    av[0] *= 38068692544
    av[1] *= 3364
    av[2] *= 11316496
    av[3] *= 128063081718016
    av[4] *= 656356768
    av[5] *= 7427658739644928
    av[6] *= 195112
    av[7] *= 2207984167552
    av[8] *= 58
    av[9] *= 1
    av = sum(av) - 100618342136696320
    av = av ^ 0b1010100100111011001100100100
    return av
