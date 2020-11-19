def main():
    cases = int(input())
    for n in range(cases):
        stores = int(input())
        values = input().split()
        for i in range(stores):
            values[i] = int(values[i])
        values.sort()
        print(str(2 * (values[stores - 1] - values[0])))


if __name__ == "__main__":
    main()
