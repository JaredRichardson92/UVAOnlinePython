skyline = []


def addBuilding(x1, h, x2):
    # Ensures there is adequate empty space in the array for new building
    while skyline.__len__() <= x2:
        skyline.append(0)

    # sets height in position array if taller than current building or if no building present
    for x in range(x1, x2):
        if h > skyline[x]:
            skyline[x] = h


def outputSkyline():
    outString = ""
    currentHeight = 0
    # Builds string by detecting location and height when hegith changes
    for i in range(0, skyline.__len__()):
        if skyline[i] != currentHeight:
            outString = outString + str(i) + " " + str(skyline[i]) + " "
            currentHeight = skyline[i]
    # Returns completed string
    return outString.rstrip()


while True:
    try:
        # Reads building lines while there available.
        inputLine = input().split()
        addBuilding(int(inputLine[0]), int(inputLine[1]), int(inputLine[2]))
    except EOFError:
        # Prints out skyline and terminates program and EOF
        print(outputSkyline())
        break
