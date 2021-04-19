def main():
    while True:
        cheapest = 1000000
        try:
            participants, budget, hotels, weeks = map(int, input().split())
        except EOFError:
            break

        for i in range(hotels):
            #Calculate lowest cost for each hotel
            perPerson = int(input())
            availRooms = input().split() 
            if perPerson * participants > budget:
                continue
            for room in availRooms:
                if int(room) < participants:
                    continue
                if participants * perPerson < cheapest:
                    cheapest = participants * perPerson


        if cheapest == 1000000:
            print("stay home")
        else:
            print(str(cheapest))




if __name__ == "__main__":
    main()