def main():
    numCommands = int(input())
    while numCommands != 0:
        currentPos = list("+x")
        rawCommands = input().split()
        commands = []
        for r in rawCommands:
            commands.append(list(r))
        for c in commands:
            # if a no command
            if c[0] == "N":
                continue
            # if starting facing X position
            elif currentPos[1] == "x":
                currentPos[1] = c[1]
                if currentPos[0] == "+":
                    currentPos[0] = c[0]
                else:
                    if c[0] == "-":
                        currentPos[0] = "+"
                    else:
                        currentPos[0] = "-"
            # Starting facing a Y direction
            elif currentPos[1] == "y":
                if c[1] == "y":
                    currentPos[1] = "x"
                    if currentPos[0] == "-":
                        currentPos[0] = c[0]
                    else:
                        if c[0] == "+":
                            currentPos[0] = "-"
                        else:
                            currentPos[0] = "+"
            # Starting facing a Z direction
            else:
                if c[1] == "z":
                    currentPos[1] = "x"
                    if currentPos[0] == "-":
                        currentPos[0] = c[0]
                    else:
                        if c[0] == "+":
                            currentPos[0] = "-"
                        else:
                            currentPos[0] = "+"

        print("".join(currentPos).capitalize())
        numCommands = int(input())


if __name__ == "__main__":
    main()