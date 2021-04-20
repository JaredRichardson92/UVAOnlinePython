def main():
    while True:
        try:
            numClasses, numCatagories = map(int, input().split())
        except (ValueError, EOFError) as e:
            exit()

        reqsMet = True
        classesTaken = input().split()
        for catagory in range(numCatagories):
            inputLine = input().split()
            catClasses = int(inputLine[0])
            reqClasses = int(inputLine[1])
            for i in range(numClasses):
                try:
                    inputLine.index(classesTaken[i])
                    reqClasses -= 1
                except ValueError:
                    pass

            if reqClasses > 0:
                reqsMet = False

        print("yes" if reqsMet else "no")


if __name__ == "__main__":
    main()