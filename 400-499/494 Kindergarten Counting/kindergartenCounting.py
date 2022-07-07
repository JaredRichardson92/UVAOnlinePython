# 494


def main():
    while True:
        try:
            line = input()
            count = 0
            lastAlpha = False
            for char in line:
                if char.isalpha() and not lastAlpha:
                    lastAlpha = True
                    count += 1
                elif not char.isalpha():
                    lastAlpha = False

            print(count)

        except EOFError:
            break


if __name__ == "__main__":
    main()
