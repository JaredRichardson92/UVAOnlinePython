def main():
    cases = int(input())
    for n in range(cases):
        input()
        if n > 0:
            print()
        cols = int(input())
        closable = True
        a, b = map(int, input().split())
        dif = a - b
        for i in range(cols - 1):
            a, b = map(int, input().split())
            if a - b != dif:
                closable = False
        print("yes" if closable else "no")


if __name__ == "__main__":
    main()