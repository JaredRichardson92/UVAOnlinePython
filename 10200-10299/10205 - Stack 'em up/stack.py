def whichCard(card):
    if (card - 1) // 13 == 0:
        suite = "Clubs"
    elif (card - 1) // 13 == 1:
        suite = "Diamonds"
    elif (card - 1) // 13 == 2:
        suite = "Hearts"
    else:
        suite = "Spades"

    val = card % 13

    if val == 0:
        face = "Ace"
    elif val > 9:
        if val == 10:
            face = "Jack"
        elif val == 11:
            face = "Queen"
        else:
            face = "King"
    else:
        face = str(val + 1)

    return face + " of " + suite


def main():
    cases = int(input())
    input()
    for c in range(cases):
        deck = [x for x in range(1, 53)]
        numShuffles = int(input())
        shuffles = []
        for i in range(numShuffles):
            shuffles.append([])
            while len(shuffles[i]) < 52:
                inVals = list(map(int, input().split()))
                while len(inVals) > 0:
                    shuffles[i].append(inVals.pop(0))

        s = input()
        while s != "":
            tmp = []
            for i in range(52):
                tmp.append(deck[shuffles[int(s) - 1][i] - 1])

            for i in range(52):
                deck[i] = tmp[i]

            try:
                s = input()
            except EOFError:
                break

        for card in deck:
            print(whichCard(card))

        if c < cases - 1:
            print()


if __name__ == "__main__":
    main()
