# 499


def main():
    while True:
        try:
            inline = input()
            letters = {}
            for char in inline:
                if char.isalpha():
                    if char not in letters.keys():
                        letters[char] = 1
                    else:
                        letters[char] += 1

            maxFreq = max(letters.values())
            maxLetters = [i for i, j in letters.items() if j == maxFreq]
            maxLetters.sort()

            out = ""
            for l in maxLetters:
                out += l
            out += " " + str(maxFreq)

            print(out)

        except EOFError:
            break


if __name__ == "__main__":
    main()
