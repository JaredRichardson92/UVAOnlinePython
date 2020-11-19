def main():
    case = 0
    while input() != '0':
        case += 1
        count = 0
        for i in input().split():
            if i != '0':
                count += 1
            else:
                count -= 1

        print("Case " + str(case) + ": " + str(count))


if __name__ == "__main__":
    main()
