def main():
    cards = list(map(int,input().split()))
    while cards[0] != 0:
        princessCards = cards[0:3]
        princeCards = cards[3:5]
        
        princessCards.sort(reverse = True)
        princeCards.sort(reverse = True)

        # print(princessCards)
        # print(princeCards)

        if princessCards[1] > princeCards[0] or (princeCards[0] < princessCards[0] and princeCards[1] < princessCards[1]):
            print(-1)
        elif princeCards[1] > princessCards[0]:
            c = 1
            while c in cards:
                c += 1
            print(c)
        elif princeCards[0] < princessCards[0] and princeCards[1] < princessCards[2]:
            print(-1)
        elif princeCards[1] > princessCards[1]:
            c = princessCards[1] + 1
            while c in cards:
                c += 1
            if c <= 52:
                print(c)
            else:
                print(-1)
            
        else:
            c = princessCards[0] + 1
            while c in cards:
                c += 1
            if c <= 52:
                print(c)
            else:
                print(-1)
        

        cards = list(map(int,input().split()))

if __name__ == "__main__":
    main()
