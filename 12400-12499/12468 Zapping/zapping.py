def main():
    a,b = map(int, input().split())
    while a != -1:
        dif = abs(a - b)
        if dif > 50:
            dif = 100 - dif
        print(str(dif))
        a, b = map(int, input().split())


if __name__ == "__main__": main()
