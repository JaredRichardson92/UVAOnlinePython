def main():

    while True:
        try:
            a, b = map(int, input().split())

            charA = "{:032b}".format(a)
            charB = "{:032b}".format(b)
            output = ""

            for i in range(32):
                binA = int(charA[i])
                binB = int(charB[i])
                val = bool(binA) != bool(binB)
                output += str(int(val))

            print(int(output, 2))

        except EOFError:
            exit()


if __name__ == "__main__":
    main()
