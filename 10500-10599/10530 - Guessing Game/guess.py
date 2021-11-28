def main():
    lowerLimit = 0
    upperLimit = 11
    guess = int(input())
    while guess != 0:
        response = input().split()[1]

        if response == "low" and guess > lowerLimit:
            lowerLimit = guess
        elif response == "high" and guess < upperLimit:
            upperLimit = guess
        elif response == "on":
            if lowerLimit >= upperLimit or upperLimit <= guess or lowerLimit >= guess:
                print("Stan is dishonest")
            else:
                print("Stan may be honest")

            lowerLimit = 0
            upperLimit = 11

        guess = int(input())


if __name__ == "__main__":
    main()
