def by_value(item):
    return item[0]

def main():
    tests = int(input())
    for i in range(tests):
        sites = {}
        for j in range(10):
            site, rank = input().split()
            sites[site] = int(rank)

        highRank = 0
        print("Case #" + str(i + 1) + ":")
        for item in sorted(sites, reverse=True, key=sites.get):
            if sites[item] >= highRank:
                highRank = sites[item]
                print(item)



if __name__ == "__main__":
    main()
