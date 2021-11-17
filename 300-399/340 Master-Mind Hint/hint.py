def main():
    n = input()
    game = 0
    while n != 0:
        game += 1
        print("Game {}:".format(game))
        passcode = list(map(int, input().split()))
        attempt = list(map(int, input().split()))
        while attempt[0] != 0:
            s = 0
            w = 0
            tempPass = passcode.copy()
            # print(len(tempPass))
            # print(len(attempt))

            for i in range(len(attempt)):
                if attempt[i] == tempPass[i]:
                    s += 1
                    attempt[i] = 0
                    tempPass[i] = 0

            for i in range(len(attempt)):
                if attempt[i] in tempPass and attempt[i] != 0:
                    tempPass.pop(tempPass.index(attempt[i]))
                    w += 1

            print("    ({},{})".format(str(s), str(w)))

            attempt = list(map(int, input().split()))
        n = int(input())


if __name__ == "__main__":
    main()
