faceCards = ["A", "K", "Q", "J", "T"]
deck = [] * 52


def cardValue(card):
    if card[0] in faceCards:
        return 10
    else:
        return int(card[0])


def whichCard(deck):
    y = 0
    index = 26
    for _ in range(3):
        x = cardValue(deck[index])
        y += x
        index -= (10 - x) + 1

    for i in range(1, 26):
        deck[index + i] = deck[26 + i]

    return deck[y - 1]


if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        deck = input().split()
        print("Case " + str(i + 1) + ": " + whichCard(deck))
