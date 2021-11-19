def getCount(grid, r, c):
    pass


def main():
    r, c = map(int, input().split())
    while r != 0:
        grid = []
        for i in range(r):
            grid.append(list(input()))

        for i in range(r):
            for j in range(c):
                if grid[i][j] != "*":
                    count = 0
        r, c = map(int, input().split())


if __name__ == "__main__":
    main()
