combinations = ['BCG', 'BGC', 'CBG', 'CGB', 'GBC', 'GCB']


class Bin():
    def __init__(self, n, b, g, c):
        self.index = n
        self.bottles = {'B': b, 'G': g, 'C': c}


def sortBottles(colorOrder, sortingBins):
    totalMoves = 0
    for bin in sortingBins:
        for bin2 in sortingBins:
            if bin != bin2:
                totalMoves += bin2.bottles[colorOrder[bin.index]]

    return totalMoves


while True:
    try:
        inputLine = input().split()
        totalMoves = 0
    except EOFError:
        break

    minMoves = ['NNN', float('inf')]
    bins = [Bin(0, int(inputLine[0]), int(inputLine[1]), int(inputLine[2])),
            Bin(1, int(inputLine[3]), int(inputLine[4]), int(inputLine[5])),
            Bin(2, int(inputLine[6]), int(inputLine[7]), int(inputLine[8]))]

    for combo in combinations:
        if sortBottles(combo, bins) < minMoves[1]:
            minMoves = [combo, sortBottles(combo, bins)]

    print(minMoves[0] + " " + str(minMoves[1]))
