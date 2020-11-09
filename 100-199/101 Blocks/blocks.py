workArea = []


class Pile:
    def __init__(self, p, b):
        self.position = p
        self.contents = [b]

    def __str__(self):
        output = str(self.position) + ":"
        for index in range(self.contents.__len__()):
            output = output + " " + str(self.contents[index])

        return output


def printBoard():
    for pile in workArea:
        print(str(pile))


def processCommand(primaryCommand, movingBlock, secondaryCommand, destinationBlock):
    # locate pile containing moving block and pile containing destination block
    for pile in workArea:
        if pile.contents.count(int(movingBlock)):
            originPile = pile.position
        if pile.contents.count(int(destinationBlock)):
            destinationPile = pile.position

    if originPile == destinationPile:
        return

    # move command indicates to clear off top of origin block before moving
    if primaryCommand == "move":
        while int(workArea[int(originPile)].contents[-1]) != int(movingBlock):
            tempBlock = workArea[int(originPile)].contents.pop()
            workArea[int(tempBlock)].contents.append(tempBlock)

    # onto secondary command indicates to clear off top of destination block before moving
    if secondaryCommand == "onto":
        while int(workArea[int(destinationPile)].contents[-1]) != int(destinationBlock):
            tempBlock = workArea[int(destinationPile)].contents.pop()
            workArea[int(tempBlock)].contents.append(tempBlock)

    # perform move
    blockShuttle = [workArea[originPile].contents.pop()]
    while int(blockShuttle[-1]) != int(movingBlock):
        blockShuttle.append(workArea[originPile].contents.pop())

    while blockShuttle.__len__() > 0:
        workArea[destinationPile].contents.append(blockShuttle.pop())


while True:
    try:
        n = int(input().split()[0])
    except EOFError:
        break

    workArea = []
    for i in range(n):
        workArea.append(Pile(i, i))

    nextCommand = input().split()
    while nextCommand[0] != "quit":
        processCommand(nextCommand[0], nextCommand[1], nextCommand[2], nextCommand[3])
        nextCommand = input().split()

    printBoard()
