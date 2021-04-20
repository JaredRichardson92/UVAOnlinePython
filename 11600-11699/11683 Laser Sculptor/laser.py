def main():
    height, width = map(int, input().split())
    while height != 0:
        cuts = list(map(int, input().split()))
        cuts.append(height)
        count = 0

        for i in range(len(cuts) - 1):
            if cuts[i + 1] > cuts[i]:
                count += cuts[i + 1] - cuts[i]

        print(str(count))
        height, width = map(int, input().split())


if __name__ == "__main__":
    main()
