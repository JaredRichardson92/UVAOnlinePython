def main():
    case = 0
    for n in range(int(input())):
        case += 1
        salaries = input().split()
        for i in range(salaries.__len__()):
            salaries[i] = int(salaries[i])
        salaries.sort()
        print("Case " + str(case) + ": " + str(salaries[1]))


if __name__ == "__main__":
    main()