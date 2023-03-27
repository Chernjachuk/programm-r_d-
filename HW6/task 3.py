def bolshe(numList):
    summa = 0
    for i in numList:

        if summa < i:
            summa = i
    return summa


print(bolshe([12, 0, 31, 2, 1, 192, -5]))
