def main():
    cases = int(input())
    for c in range(cases):
        n, k, p = map(int, input().split())
        lastPlayer = ((k + p) % n) if ((k + p) % n) else n
        print(f"Case {c+1}: {lastPlayer}")


if __name__ == "__main__":
    main()
