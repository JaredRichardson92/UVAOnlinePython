def main():
    banks, debentures = map(int, input().split())
    while banks != 0:
        values = input().split()
        for i, val in enumerate(values): values[i] = int(val)
        for i in range(debentures):
            debtor, creditor, amount = map(int, input().split())
            values[debtor - 1] -= amount
            values[creditor - 1] += amount
        output = 'S'
        for i in range(values.__len__()):
            if values[i] < 0:
                output = 'N'
        print(output)
        banks, debentures = map(int, input().split())


if __name__ == "__main__":
    main()
