n, p = map(int, input().split())
proposal = 0
curCompanyCosts = [0, 0]
while n + p != 0:
    proposal += 1
    maxCompliance = 0
    bestCompany = ""
    bestCompnayCost = 0
    if proposal > 1:
        print()
    for _ in range(n):
        input()

    for _ in range(p):
        curCompany = input()
        curCompanyCosts[0], curCompanyCosts[1] = map(float, input().split())
        if curCompanyCosts[1] > maxCompliance or (
            curCompanyCosts[1] == maxCompliance and bestCompanyCost > curCompanyCosts[0]
        ):
            maxCompliance = curCompanyCosts[1]
            bestCompanyCost = curCompanyCosts[0]
            bestCompany = curCompany

        for _ in range(int(curCompanyCosts[1])):
            input()

    print("RFP #" + str(proposal))
    print(bestCompany)
    n, p = map(int, input().split())

quit
