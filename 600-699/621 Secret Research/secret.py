def decode(secretValue):
    if secretValue == '1' or secretValue == '4' or secretValue == '78':
        return '+'
    elif secretValue.endswith('35'):
        return '-'
    elif str(secretValue).startswith("9") and str(secretValue).endswith("4"):
        return '*'
    else:
        return '?'


def main():
    for n in range(int(input())):
        print(decode(input()))


if __name__ == "__main__":
    main()
