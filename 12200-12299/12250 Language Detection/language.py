def main():
    word = input()
    case = 0
    while word != '#':
        case += 1
        if word == "HELLO":
            language = "ENGLISH"
        elif word == "HOLA":
            language = "SPANISH"
        elif word == "HALLO":
            language = "GERMAN"
        elif word == "BONJOUR":
            language = "FRENCH"
        elif word == "CIAO":
            language = "ITALIAN"
        elif word == "ZDRAVSTVUJTE":
            language = "RUSSIAN"
        else:
            language = "UNKNOWN"

        print("Case " + str(case) + ": " + language)
        word = input()


if __name__ == "__main__":
    main()
