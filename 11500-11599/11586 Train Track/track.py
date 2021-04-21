def main():
    cases = int(input())
    for i in range(cases):
        tracks = input().split()
        parity = 0
        for track in tracks:
            if track[0] == track[1]:
                if track[0] == "F":
                    parity += 1
                else:
                    parity -= 1

        print("LOOP" if parity == 0 and len(tracks) > 1 else "NO LOOP")


if __name__ == "__main__":
    main()