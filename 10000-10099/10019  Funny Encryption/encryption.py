numTests = int(input())

for _ in range(numTests):
    n = int(input())

    b1 = str((str(bin(n))[2:]).count("1"))
    b2 = str((str(bin(int("0x" + str(n), 16)))[2:]).count("1"))

    print(b1 + " " + b2)
