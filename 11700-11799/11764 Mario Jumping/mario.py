def main():
    cases = int(input())
    for c in range(cases):
        input()
        jumps = input().split()
        for i in range(jumps.__len__()):
            jumps[i] = int(jumps[i])
        downJumps = 0
        upJumps = 0
        currentHeight = jumps[0]
        for i in range(1, jumps.__len__()):
            if jumps[i] > currentHeight:
                upJumps += 1
            elif jumps[i] < currentHeight:
                downJumps += 1
            currentHeight = jumps[i]

        print("Case " + str(c + 1) + ": " + str(upJumps) + " " + str(downJumps))


if __name__ == "__main__":
    main()
