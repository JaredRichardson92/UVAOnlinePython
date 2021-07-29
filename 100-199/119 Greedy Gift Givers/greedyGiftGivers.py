giftGivers = int(input())
while giftGivers > 0:
    giftValues = {}
    names = input().split()
    for i in range(len(names)):
        giftValues[names[i]] = 0

    for _ in range(giftGivers):
        gifts = input().split()
        if gifts[1] == "0" or gifts[2] == "0":
            continue

        giftValues[gifts[0]] -= int(gifts[2]) * int(int(gifts[1]) / int(gifts[2]))
        for i in range(int(gifts[2])):
            giftValues[gifts[i + 3]] += int(int(gifts[1]) / int(gifts[2]))

    for giver in giftValues:
        print(giver + " " + str(giftValues[giver]))

    try:
        giftGivers = int(input())
        print()
    except EOFError:
        quit()
