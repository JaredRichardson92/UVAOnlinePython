def main():
    total = 0
    for n in range(int(input())):
        command = input().split()
        if command[0] == "donate":
            total += int(command[1])
        else:
            print(str(total))


if __name__ == "__main__":
    main()
