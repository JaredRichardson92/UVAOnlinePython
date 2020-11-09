grid = [][]


class Turtle:
    def __init__(self, x, y, dir, instructionString):
        self.pos = {x, y}
        self.dir = dir

        for i in len(instructionString):
            self.instruction = instructionString[i]
            if self.instruction == 'R':
                self.turnRight()
            elif self.instruction == 'L':
                self.turnLeft()
            elif self.instruction == 'F':
                self.turnRight()

    def turnRight(self):
        if self.dir == 'N':
            self.dir = 'E'
        elif self.dir == 'E':
            self.dir = 'S'
        elif self.dir == 'S':
            self.dir = 'W'
        else:
            self.dir = 'N'

    def turnLeft(self):
        if self.dir == 'N':
            self.dir = 'W'
        elif self.dir == 'E':
            self.dir = 'N'
        elif self.dir == 'S':
            self.dir = 'E'
        else:
            self.dir = 'S'

    def moveForward(self):




while True:
    x, y = map(int, input().split())
    grid = [x][y + 1]
    for i in range(0, x):
        for j in range(0, j):
            grid[i][j] = None

    try:
        inputLine = input().split()
        directions = input().split()
        turtle = Turtle(inputLine[0], inputLine[1], inputLine[2], directions)



    except EOFError:
        break
