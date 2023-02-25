oudler_Scores = [56, 51, 41, 36]
oudlers = ["twenty-one", "one", "fool"]


def main():
    test = int(input())
    for case in range(test):
        if case > 0:
            print()
        num_cards = int(input())
        score = 0
        oudler_count = 0
        for _ in range(num_cards):
            card = input().split()[0]
            if card in oudlers:
                oudler_count += 1
                score += 4.5
            elif card == "king":
                score += 4.5
            elif card == "queen":
                score += 3.5
            elif card == "knight":
                score += 2.5
            elif card == "jack":
                score += 1.5
            else:
                score += 0.5

        print(f"Hand #{case + 1}")
        print(
            "Game "
            + ("won " if score >= oudler_Scores[oudler_count] else "lost ")
            + "by "
            + f"{abs(int(score - oudler_Scores[oudler_count]))} point(s)."
        )


if __name__ == "__main__":
    main()
