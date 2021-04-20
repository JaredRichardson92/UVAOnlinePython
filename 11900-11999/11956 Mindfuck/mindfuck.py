def main():
    cases = int(input())
    for c in range(cases):
        arr = bytearray(100)
        pointer = 0
        instructions = input()
        for i in range(len(instructions)):

            if instructions[i] == ">":
                pointer += 1
                if pointer == 100:
                    pointer = 0
            elif instructions[i] == "<":
                pointer -= 1
                if pointer == -1:
                    pointer = 99
            elif instructions[i] == "+":
                try:
                    arr[pointer] += 1
                except ValueError:
                    arr[pointer] = 0
            elif instructions[i] == "-":
                try:
                    arr[pointer] -= 1
                except ValueError:
                    arr[pointer] = 255

        output = "Case " + str(c + 1) + ":"
        for i in range(len(arr)):
            output += " " + ("%0.2X" % arr[i]).upper()
        print(output)


if __name__ == "__main__":
    main()