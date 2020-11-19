def main():
    for n in range(int(input())):
        j, k = map(int, input().split())
        if j < k:
            print("<")
        elif j > k:
            print(">")
        else:
            print("=")


if __name__ == "__main__":
    main()
