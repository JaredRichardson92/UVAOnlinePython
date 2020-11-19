def main():
    for n in range(int(input())):
        row, col = map(int, input().split())
        if (row - 2) % 3 == 0:
            cRow = (row - 2) // 3
        else:
            cRow = ((row - 2) // 3) + 1
        if (col - 2) % 3 == 0:
            cCol = (col - 2) // 3
        else:
            cCol = ((col - 2) // 3) + 1
        print(str(cRow * cCol))


if __name__ == "__main__":
    main()
