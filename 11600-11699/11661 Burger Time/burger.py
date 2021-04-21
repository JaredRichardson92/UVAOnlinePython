def main():
    hwLength = int(input())
    while hwLength > 0:
        hw = input()
        try:
            hw.index("Z")
            print(0)
            hwLength = int(input())
            continue
        except ValueError:
            pass

        restaurants = []
        drugstores = []
        for i in range(len(hw)):
            if hw[i] == "D":
                drugstores.append(i)
            elif hw[i] == "R":
                restaurants.append(i)

        shortest = hwLength
        for p in range(len(drugstores)):
            for r in range(len(restaurants)):
                if abs(drugstores[p] - restaurants[r]) < shortest:
                    shortest = abs(drugstores[p] - restaurants[r])

        print(shortest)
        hwLength = int(input())


if __name__ == "__main__":
    main()