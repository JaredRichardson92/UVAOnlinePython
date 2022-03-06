def whichCard(val):
    if val // 13 == 0:
        suite = "Clubs"
    elif val // 13 == 1:
        suite = "Diamonds"
    elif val // 13 == 2:
        suite = "Hearts"
    else:
        suite = "Spades"

    face = (val % 13) + 1
    if face == 1:
        face = "Ace"
    elif face > 10:
        if face == 11:
            face = "Jack"
        elif face == 12:
            face = "Queen"
        else:
            face = "King"

    return str(face) + " of " + suite


def main():
    scenarios = int(input())
    input()
    for _ in range(scenarios):
        shuffles = []
        numShuffles = input()
        deck = [x for x in range(1, 53)]

        for _ in range(numShuffles):
            shuffles.append(map(int, inString.split()))
            inString = input()

        shuff = input()
        while shuff != "":
            temp = []
            for i in range(52):
                temp.append(deck[shuffles[shuff - 1][i] - 1])

            for i in range(temp.length()):
                deck[i] = temp[i]

        for card in deck:
            print(whichCard(card))


if __name__ == "__main__":
    main()
