def getTop(grid, row, col):
    count = 0
    if row > 0:
        if grid[row - 1][col] == "*":
            count += 1

    return count


def getBott(grid, row, col):
    count = 0
    if row < len(grid) - 1:
        if grid[row + 1][col] == "*":
            count += 1

    return count


def getLeft(grid, row, col):
    if col == 0:
        return 0
    else:
        count = 0
        if grid[row][col - 1] == "*":
            count += 1
        if row > 0 and grid[row - 1][col - 1] == "*":
            count += 1
        if row < len(grid) - 1 and grid[row + 1][col - 1] == "*":
            count += 1

        return count


def getRight(grid, row, col):
    if col == len(grid[0]) - 1:
        return 0
    else:
        count = 0
        if grid[row][col + 1] == "*":
            count += 1
        if row > 0 and grid[row - 1][col + 1] == "*":
            count += 1
        if row < len(grid) - 1 and grid[row + 1][col + 1] == "*":
            count += 1

        return count


def getCount(grid, row, col):
    return (
        getTop(grid, row, col)
        + getBott(grid, row, col)
        + getLeft(grid, row, col)
        + getRight(grid, row, col)
    )


def main():
    r, c = map(int, input().split())
    counter = 0
    while r != 0:
        counter += 1
        grid = []
        for i in range(r):
            grid.append(list(input()))

        for i in range(r):
            for j in range(c):
                if grid[i][j] != "*":
                    count = getCount(grid, i, j)
                    grid[i][j] = count

        print("Field #{}:".format(counter))
        for row in grid:
            outString = ""
            for val in row:
                outString = outString + str(val)
            print(outString)

        r, c = map(int, input().split())
        if r == 0:
            break
        print()


if __name__ == "__main__":
    main()
