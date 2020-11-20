def main():
    for n in range(int(input())):
        location = 0
        instructions = []
        for i in range(int(input())):
            inst = input().strip()
            if inst[0] == 'L':
                location -= 1
                instructions.append('L')
            elif inst[0] == 'R':
                location += 1
                instructions.append('R')
            else:
                var = instructions[int(inst.split()[2]) - 1]
                if var == 'L':
                    location -= 1
                    instructions.append('L')
                elif var == 'R':
                    location += 1
                    instructions.append('R')

        print(str(location))


if __name__ == "__main__":
    main()
