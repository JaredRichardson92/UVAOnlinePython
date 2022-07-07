# 162


faceCards = {"J": 1, "Q": 2, "K": 3, "A": 4}


def main():
    cardsIn = input()
    while not cardsIn.startswith("#"):
        # Get cards from current line and next 3 lines
        deck = cardsIn.split()
        for _ in range(3):
            for card in input().split():
                deck.append(card)

        # Deals cards and setups game variables
        p2deck = deck[::2]
        p1deck = deck[1::2]
        p1deck.reverse()
        p2deck.reverse()
        playerDecks = [p1deck, p2deck]
        turnCounter = 1
        toCover = 0
        playDeck = []

        while len(playerDecks[turnCounter % 2]) > 0:
            # Game loop
            currPlayerIndex = turnCounter % 2
            if toCover > 0:
                while toCover > 0:
                    if len(playerDecks[currPlayerIndex]) > 0:
                        playDeck.append(playerDecks[currPlayerIndex].pop(0))
                        if playDeck[-1][1] in faceCards.keys():
                            toCover = faceCards[playDeck[-1][1]]
                            break
                        toCover -= 1
                    else:
                        break

                if toCover == 0:
                    for card in playDeck:
                        playerDecks[(turnCounter + 1) % 2].append(card)
                    playDeck = []

                elif (
                    len(playerDecks[currPlayerIndex]) == 0
                    and playDeck[-1][1] not in faceCards.keys()
                ):
                    break

            else:
                playDeck.append(playerDecks[currPlayerIndex].pop(0))
                if playDeck[-1][1] in faceCards.keys():
                    toCover = faceCards[playDeck[-1][1]]

            turnCounter += 1

        # Print winner and their deck size
        winnerIndex = (turnCounter + 1) % 2
        print(f"{winnerIndex + 1}{len(playerDecks[winnerIndex]):>3}")

        # Start next round
        cardsIn = input()


if __name__ == "__main__":
    main()
