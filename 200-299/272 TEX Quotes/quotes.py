opening = True


def quotations(sentence):
    global opening
    count = 0
    for i in range (sentence.__len__()):
        if sentence[i] == '"':
            count += 1

    offset = 0
    for i in range(count):
        if opening:
            sentence = sentence.replace('"', "``", 1)
        else:
            sentence = sentence.replace('"', "''", 1)

        opening = not opening

    print(sentence)


while True:
    try:
        readLine = input()
        quotations(readLine)
    except EOFError:
        break
