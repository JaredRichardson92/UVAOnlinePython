import math


def main():
    while True:
        prev = input()
        if prev.__contains__("END"):
            exit()

        value = str(len(prev))
        count = 1
        while value != prev:
            prev = value
            value = str(len(prev))
            count += 1
        print(count)


if __name__ == "__main__":
    main()
