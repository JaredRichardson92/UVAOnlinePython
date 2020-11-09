# Listing out all combinations since relatively small amount
combinations = ['BCG', 'BGC', 'CBG', 'CGB', 'GBC', 'GCB']


class RecycleBin:
    # Index is location of bin and dictionary containing quantity for each color type
    def __init__(self, n, b, g, c):
        self.index = n
        self.bottles = {'B': b, 'G': g, 'C': c}


def sortBottles(colorOrder, sortingBins):
    totalMoves = 0
    # calculates total number of moves required to achieve provided color order with given bins
    for bin1 in sortingBins:
        for bin2 in sortingBins:
            if bin1 != bin2:
                totalMoves += bin2.bottles[colorOrder[bin1.index]]

    return totalMoves


while True:
    try:
        # Reads input line
        inputLine = input().split()
        # Infinitely large number so all sorts will be smaller and arbitrary order for smallest sort.
        minMoves = ['NNN', float('inf')]
        # SortingBin array created from input
        bins = [RecycleBin(0, int(inputLine[0]), int(inputLine[1]), int(inputLine[2])),
                RecycleBin(1, int(inputLine[3]), int(inputLine[4]), int(inputLine[5])),
                RecycleBin(2, int(inputLine[6]), int(inputLine[7]), int(inputLine[8]))]
        # Iterates through all permutations and keeps track of smallest number of moves and respective order
        for combo in combinations:
            if sortBottles(combo, bins) < minMoves[1]:
                minMoves = [combo, sortBottles(combo, bins)]
        # Outputs color order and prints
        print(minMoves[0] + " " + str(minMoves[1]))

    except EOFError:
        # Terminates program at end EOF
        break
