def main():
    call = input()
    case = 0
    while call != "*":
        case += 1
        reply = "Akbar" if call == "Hajj" else "Asghar"
        print("Case " + str(case) + ": Hajj-e-" + reply)
        call = input()


if __name__ == "__main__":
    main()

# TEST
