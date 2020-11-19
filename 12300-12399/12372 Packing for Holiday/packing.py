def main():
    case = 0
    for i in range(int(input())):
        case += 1
        box = input().split()
        if int(box[0]) > 20 or int(box[1]) > 20 or int(box[2]) > 20:
            result = "bad"
        else:
            result = "good"

        print("Case " + str(case) + ": " + result)


if __name__ == "__main__":
    main()
