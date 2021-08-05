suites = ["C", "D", "H", "S"]
values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

outStr = ""

for i in range(4):
    for j in range(13):
        outStr = outStr + values[j] + suites[i] + " "

print(outStr)
