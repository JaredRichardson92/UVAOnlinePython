import copy


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
    runs = int(input())
    for n in range(runs):
        # Load bomb locations
        input()
        size = int(input())
        grid = []
        for _ in range(size):
            grid.append(list(input()))

        bombsShowing = False
        bombGrid = copy.deepcopy(grid)
        # Add counts
        for i in range(size):
            for j in range(size):
                if grid[i][j] != "*":
                    grid[i][j] = getCount(grid, i, j)

        # Cover unkown tiles
        for i in range(size):
            line = list(input())
            for j in range(size):
                if not bombsShowing and line[j] == "x" and grid[i][j] == "*":
                    bombsShowing = True
                if line[j] == ".":
                    grid[i][j] = "."

        # Reveals bombs if bombs showing
        if bombsShowing:
            for i in range(size):
                for j in range(size):
                    if bombGrid[i][j] == "*":
                        grid[i][j] = "*"

        # Print Grid
        for i in range(size):
            out = ""
            for j in range(size):
                out += str(grid[i][j])
            print(out)

        if n < runs - 1:
            print()


if __name__ == "__main__":
    main()
