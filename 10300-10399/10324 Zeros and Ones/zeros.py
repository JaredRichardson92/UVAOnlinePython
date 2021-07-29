caseNum = 0
while True:
    try:
        inString = input()
        valMap = [0] * len(inString)
        for i in range(1, len(inString)):
            if inString[i] == inString[i - 1]:
                valMap[i] = valMap[i - 1]
            else:
                valMap[i] = valMap[i - 1] + 1

        caseNum += 1
        print("Case " + str(caseNum) + ":")
        testCases = int(input())
        for _ in range(testCases):
            v1, v2 = map(int, input().split())
            if valMap[v1] == valMap[v2]:
                print("Yes")
            else:
                print("No")

    except EOFError:
        quit()
    except Exception as e:
        print(e)
        quit()
