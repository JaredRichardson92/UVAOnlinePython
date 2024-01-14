def main():
    numTests = int(input())

    for _ in range(numTests):
        n = int(input())

        binN = str(bin(n))[2:]
        hexN = str(bin(int("0x" + str(n), 16)))[2:]

        b1 = str(binN.count("1"))
        b2 = str(hexN.count("1"))

        print(b1 + " " + b2)


if __name__ == "__main__":
    main()
