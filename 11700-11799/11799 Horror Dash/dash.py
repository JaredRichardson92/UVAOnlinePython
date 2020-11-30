def main():
    cases = int(input())
    for i in range(cases):
        race = input().split()
        for v in range(race.__len__()):
            race[v] = int(race[v])
        race.sort()
        print("Case " + str(i + 1) + ": " + str(race[race.__len__() - 1]))


if __name__ == "__main__":
    main()
