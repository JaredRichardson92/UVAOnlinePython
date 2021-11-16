notes = {
    "W": 1,
    "H": float(1 / 2),
    "Q": float(1 / 4),
    "E": float(1 / 8),
    "S": float(1 / 16),
    "T": float(1 / 32),
    "X": float(1 / 64),
}


def main():
    music = input()
    while music != "*":
        fullMeasures = 0
        count = 0

        for char in music:
            if char == "/":
                if count == 1:
                    fullMeasures += 1
                count = 0
            else:
                count += notes[char]

        print(str(fullMeasures))
        music = input()


if __name__ == "__main__":
    main()
