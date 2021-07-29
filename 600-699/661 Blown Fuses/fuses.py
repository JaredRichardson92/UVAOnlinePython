def runScenario(n, m, c, case):
    deviceStatus = [-1] * n
    deviceDraw = []
    deviceInstructions = []
    currentUse = 0
    currentMax = 0

    print("Sequence " + str(case))

    for _ in range(n):
        deviceDraw.append(int(input()))

    for _ in range(m):
        deviceInstructions.append(int(input()))

    for d in deviceInstructions:
        deviceStatus[d - 1] *= -1
        currentUse += deviceDraw[d - 1] * deviceStatus[d - 1]

        if currentUse > c:
            print("Fuse was blown.\n")
            return
        elif currentUse > currentMax:
            currentMax = currentUse

    print("Fuse was not blown.")
    print("Maximal power consumption was " + str(currentMax) + " amperes.\n")
    return


if __name__ == "__main__":
    caseNumber = 0
    n, m, c = map(int, input().split())
    while n + m + c != 0:
        caseNumber += 1
        runScenario(n, m, c, caseNumber)
        n, m, c = map(int, input().split())
