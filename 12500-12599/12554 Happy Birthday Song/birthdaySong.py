words = ['Happy', 'birthday', 'to',  'you', 'Happy', 'birthday', 'to', 'you', 'Happy', 'birthday', 'to', 'Rujia', 'Happy', 'birthday', 'to', 'you']
people = []


def main():
    for n in range(int(input())):
        people.append(input())

    lines = 0
    while lines < people.__len__() or lines % words.__len__() != 0:
        print(people[lines % people.__len__()] + ": " + words[lines % words.__len__()])
        lines += 1


if __name__ == "__main__":
    main()
