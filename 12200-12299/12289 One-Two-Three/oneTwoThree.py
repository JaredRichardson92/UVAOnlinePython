def main():
    for n in range(int(input())):
        word = input()
        calc = 0
        if word.__len__() == 5:
            print("3")
        else:
            if word[0] == 'o':
                calc += 1
            elif word [0] == 't':
                calc -= 1
            if word[1] == 'n':
                calc += 1
            elif word[1] == 'w':
                calc -= 1
            if word[2] == 'e':
                calc += 1
            elif word [2] == 'o':
                calc -= 1

            if calc > 0:
                print("1")
            else:
                print("2")


if __name__ == "__main__":
    main()
