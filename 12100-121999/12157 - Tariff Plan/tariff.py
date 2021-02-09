def miles(calls):
    cost = 0
    for call in calls:
        cost += (int(int(call) / 30) + 1) * 10
    return cost


def juice(calls):
    cost = 0
    for call in calls:
        cost += (int(int(call) / 60) + 1) * 15
    return cost


def main():
    cases = int(input())
    for i in range(cases):
        input()
        calls = input().split()
        milesCost = miles(calls)
        juiceCost = juice(calls)
        if milesCost > juiceCost:
            print("Case " + str(int(i) + 1) + ": " + "Juice " + str(juiceCost))
        elif juiceCost > milesCost:
            print("Case " + str(int(i) + 1) + ": " + "Mile " + str(milesCost))
        else:
            print("Case " + str(int(i) + 1) + ": " + "Mile Juice " + str(milesCost))


if __name__ == "__main__":
    main()
