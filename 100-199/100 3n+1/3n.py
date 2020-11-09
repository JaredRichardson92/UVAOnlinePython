a = {}


def calcCycle(x):
    if x in a:
        return a[x]
    elif x == 1:
        return 1
    elif x % 2 == 0:
        y = x / 2
    else:
        y = (3 * x) + 1

    a[x] = calcCycle(y) + 1
    return a[x]


while True:
    try:
        x, y = map(int, input().split())
    except EOFError:
        break

    maxCycle = 0
    for i in range(min(x, y), max(x, y) + 1):
        n = calcCycle(i)
        if n > maxCycle:
            maxCycle = n

    print(x, y, maxCycle)
