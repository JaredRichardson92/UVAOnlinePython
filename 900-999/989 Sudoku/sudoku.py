size = 0
grid = []
solved = False


def fillGrid():
    global size, grid
    grid = []
    inLine = []
    for i in range(size * size):
        grid.append([])
        inLine = input().split()
        for j in range(size * size):
            grid[i].append(int(inLine[j]))


def printGrid():
    global size, grid
    for i in range(size * size):
        output = ""
        for j in range(size * size):
            output = output + str(grid[i][j]) + " "
        print(output.strip())


def possibleValue(r, c, n):
    global size, grid
    for i in range(size * size):
        if grid[r][i] == n:
            return False

    for i in range(size * size):
        if grid[i][c] == n:
            return False

    R0 = r // size
    C0 = c // size
    for i in range(size):
        for j in range(size):
            if grid[(size * R0) + i][(size * C0) + j] == n:
                return False

    return True


def solveGrid():
    global size, grid, solved
    for r in range(size * size):
        for c in range(size * size):
            if grid[r][c] == 0:
                for n in range(1, 1 + (size * size)):
                    if possibleValue(r, c, n):
                        grid[r][c] = n
                        solveGrid()
                        if solved:
                            return
                        else:
                            grid[r][c] = 0
                return

    solved = True
    return


def main():
    global size, grid, solved
    while True:
        try:
            solved = False
            size = int(input())
            fillGrid()
            solveGrid()
            if solved:
                printGrid()
            else:
                print("NO SOLUTION")
            input()
            print()
        except EOFError:
            return


if __name__ == "__main__":
    main()
