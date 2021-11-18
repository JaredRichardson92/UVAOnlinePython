from itertools import product


def getHint(password, guess):
    s = 0
    w = 0
    tmpGuess = guess.copy()

    for i in range(len(tmpGuess)):
        if tmpGuess[i] == password[i]:
            s += 1
            tmpGuess[i] = 0
            password[i] = 0

    for i in range(len(tmpGuess)):
        if tmpGuess[i] in password and tmpGuess[i] != 0:
            password.pop(password.index(tmpGuess[i]))
            w += 1

    return (s, w)


def getCount(guess, s, w):
    count = 0
    guess = [int(a) for a in str(guess)]

    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for combo in list(product(vals, repeat=len(guess))):
        hint = getHint(list(combo), guess)
        if s == hint[0] and w == hint[1]:
            count += 1

    return count


def main():
    cases = int(input())
    for i in range(cases):
        testPass, testS, testW = map(int, input().split())
        print(getCount(testPass, testS, testW))


if __name__ == "__main__":
    main()
