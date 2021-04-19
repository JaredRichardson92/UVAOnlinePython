def ordered(heights):
    correct = True
    if int(heights[0]) < int(heights[1]):
        for i in range(heights.__len__() - 1):
            if int(heights[i]) > int(heights[i + 1]):
                correct = False
                break
    else:
        for i in range(heights.__len__() - 1):
            if int(heights[i]) < int(heights[i + 1]):
                correct = False
                break

    print("Ordered" if correct else "Unordered")


def main():
    print("Lumberjacks:")
    cases = int(input())
    for i in range(cases):
        lumberJacks = input().split()
        ordered(lumberJacks)


if __name__ == "__main__": main()
