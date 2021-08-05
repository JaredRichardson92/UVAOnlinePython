steps = int(input())


def north():
    temp = sides["t"]
    sides["t"] = sides["s"]
    sides["s"] = sides["b"]
    sides["b"] = sides["n"]
    sides["n"] = temp


def south():
    temp = sides["t"]
    sides["t"] = sides["n"]
    sides["n"] = sides["b"]
    sides["b"] = sides["s"]
    sides["s"] = temp


def east():
    temp = sides["t"]
    sides["t"] = sides["w"]
    sides["w"] = sides["b"]
    sides["b"] = sides["e"]
    sides["e"] = temp


def west():
    temp = sides["t"]
    sides["t"] = sides["e"]
    sides["e"] = sides["b"]
    sides["b"] = sides["w"]
    sides["w"] = temp


while steps != 0:
    # Dice Faces Top, North, West, South, East, Bottom
    sides = {"t": 1, "n": 2, "w": 3, "s": 5, "e": 4, "b": 6}
    for _ in range(steps):
        direction = input()[0]
        if direction == "n":
            north()
        elif direction == "s":
            south()
        elif direction == "e":
            east()
        else:
            west()

    print(str(sides["t"]))
    steps = int(input())
