def g(value):
    if value.__len__() == 1:
        return value
    digits = 0
    for place in range(value.__len__()):
        digits += int(value[place])
    return g(str(digits))


def main():
    val = input()
    while val != '0':
        print(g(val))
        val = input()


if __name__ == "__main__":
    main()
