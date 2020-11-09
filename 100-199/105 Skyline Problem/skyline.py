skyline = []


def addBuilding(x1, h, x2):
    while skyline.__len__() <= x2:
        skyline.append(0)

    for x in range(x1, x2):
        if h > skyline[x]:
            skyline[x] = h


def outputSkyline():
    outString = ""
    currentHeight = 0
    for i in range(0, skyline.__len__()):
        if skyline[i] > currentHeight:
            outString = outString + str(i) + " " + str(skyline[i]) + " "
        elif skyline[i] < currentHeight:
            outString = outString + str(i) + " " + str(skyline[i]) + " "

        currentHeight = skyline[i]

    return outString.rstrip()


while True:
    try:
        inputLine = input().split()
    except EOFError:
        print(outputSkyline())
        break

    addBuilding(int(inputLine[0]), int(inputLine[1]), int(inputLine[2]))
