def main():
    cases = int(input())
    for i in range(cases):
        values = input().split()
        numPlayers = int(values.pop(0))
        values.sort()
        print(f"Case {i+1}: {values[numPlayers // 2]}")


if __name__ == "__main__":
    main()
