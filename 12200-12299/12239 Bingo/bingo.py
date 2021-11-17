def main():
    n, b = map(int, input().split())
    while n != 0:
        temp = input().split()
        balls = list(map(int, temp))
        balls.sort()
        # Process
        for i in range(b):
            for j in range(i + 1, b):
                val = abs(balls[i] - balls[j])
                if val not in balls:
                    balls.append(val)

        print("Y") if len(balls) >= n + 1 else print("N")

        # Process
        n, b = map(int, input().split())


if __name__ == "__main__":
    main()
