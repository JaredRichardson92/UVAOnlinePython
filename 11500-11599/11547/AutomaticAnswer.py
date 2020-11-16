def main():
    test = int(input())

    for i in range(test):
        n = int(input())
        val = (315 * n) + 36962
        if val < 0:
            val = val * -1
        print(int((val // 10) % 10))


if __name__ == "__main__":
    main()
