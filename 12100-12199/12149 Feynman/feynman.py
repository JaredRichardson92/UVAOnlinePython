def main():
    board = int(input())
    while board != 0:
        val = int((board * (board + 1) * (2 * board + 1)) / 6)
        print(val)
        board = int(input())


if __name__ == "__main__":
    main()
