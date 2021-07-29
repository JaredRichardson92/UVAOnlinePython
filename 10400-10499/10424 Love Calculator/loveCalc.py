def calcName(name):
    name = name.lower()
    val = 0
    for c in name:
        if ord(c) > 96 and ord(c) < 123:
            val += (ord(c)-96)

    while val > 9:
        temp = str(val)
        val = 0
        for c in temp:
            val += int(c)

    return val

while True:
    try:
        value1 = calcName(input())
        value2 = calcName(input())
        ratio = value1/value2
        if ratio > 1:
            ratio = 1/ratio
        print("{:.2f} %".format(ratio*100))
    except EOFError:
        quit()
    except Exception as e:
        print(e)
        quit()