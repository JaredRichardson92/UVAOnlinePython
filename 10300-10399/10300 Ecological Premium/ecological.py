def main():
    for n in range(int(input())):
        total = 0
        for i in range(int(input())):
            x, y, z = map(int, input().split())
            total += x * z
        print(str(total))


if __name__ == "__main__":
    main()
