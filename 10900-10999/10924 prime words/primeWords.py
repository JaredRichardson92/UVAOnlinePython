def main():
    while True:
        try:
            word = input()
            val = 0

            for i in range(len(word)):
                val += getNumVal(word[i])

            if isPrime(val):
                print("It is a prime word.")
            else:
                print("It is not a prime word.")
        except:
            exit()


def isPrime(n) -> bool:
    prime = True
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            prime = False

    return prime


def getNumVal(letter) -> int:
    val = ord(letter)

    if val >= 97:
        return val - 96
    else:
        return val - 38


if __name__ == "__main__":
    main()
