def main():
    count = int(input())
    while count != 0:
        oX, oY = map(int, input().split())
        for i in range(count):
            hX, hY = map(int, input().split())
            if oX == hX or oY == hY:
                direction = "divisa"
            else:
                if oY > hY:
                    direction = "S"
                else:
                    direction = "N"

                if oX > hX:
                    direction = direction + "O"
                else:
                    direction = direction + "E"

            print(direction)

        count = int(input())


if __name__ == "__main__":
    main()
