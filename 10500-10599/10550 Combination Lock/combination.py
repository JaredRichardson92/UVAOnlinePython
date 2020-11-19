def main():
    lineIn = input()
    while lineIn != "0 0 0 0":
        print(calcRotations(lineIn.split()))
        lineIn = input()


def calcRotations(values):
    rotation = 1080

    for i in range(4):
        values[i] = int(values[i])

    if values[0] > values[1]:
        rotation += 9 * (values[0] - values[1])
    elif values[1] > values[0]:
        rotation += 9 * (40 - values[1] + values[0])

    if values[1] > values[2]:
        rotation += 9 * (40 - values[1] + values[2])
    elif values[2] > values[1]:
        rotation += 9 * (values[2] - values[1])

    if values[2] > values[3]:
        rotation += 9 * (values[2] - values[3])
    elif values[3] > values[2]:
        rotation += 9 * (40 - values[3] + values[2])

    return str(rotation)


if __name__ == "__main__":
    main()
