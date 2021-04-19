grid = [
    ["O", "B", "I", "D", "A", "I", "B", "K", "R"],
    ["R", "K", "A", "U", "L", "H", "I", "S", "P"],
    ["S", "A", "D", "I", "Y", "A", "N", "N", "O"],
    ["H", "E", "I", "S", "A", "W", "H", "I", "A"],
    ["I", "R", "A", "K", "I", "B", "U", "L", "S"],
    ["M", "F", "B", "I", "N", "T", "R", "N", "O"],
    ["U", "T", "O", "Y", "Z", "I", "F", "A", "H"],
    ["L", "E", "B", "S", "Y", "N", "U", "N", "E"],
    ["E", "M", "O", "T", "I", "O", "N", "A", "L"],
]
names = ["RAKIBUL", "ANINDYA", "MOSHIUR", "KABIR", "SUNNY", "OBAIDA", "WASI"]


def checkDown(i, j, name):
    if i + name.__len__() > 9:
        return False

    letters = list(name)
    for k in range(name.__len__()):
        try:
            var = letters.index(grid[i + k][j])
        except ValueError:
            return False

        letters[var] = " "

    return True


def checkRight(i, j, name):
    if j + name.__len__() > 9:
        return False

    letters = list(name)
    for k in range(name.__len__()):
        try:
            var = letters.index(grid[i][j + k])
        except ValueError:
            return False

        letters[var] = " "

    return True


def countNames(name):
    count = 0
    for i in range(9):
        for j in range(9):
            if checkRight(i, j, name):
                count += 1
            if checkDown(i, j, name):
                count += 1

    return count


def main():
    for name in names:
        if countNames(name) > 1:
            print(name)


if __name__ == "__main__":
    main()
