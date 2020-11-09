while True:
    try:
        n = int(input().split()[0])
        p = int(input().split()[0])
        val = int(p ** (1.0 / n))

        if val ** n == p:
            print(str(val))
        else:
            print(str(val+1))

    except EOFError:
        break
