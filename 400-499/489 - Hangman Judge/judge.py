def main():
    round = input()
    while round != "-1":
        print("Round", round)
        solution = list(input())
        rawGuesses = list(input())
        guesses = []
        misses = 0
        finished = False

        for g in rawGuesses:
            if g not in guesses:
                guesses.append(g)

        for guess in guesses:
            if guess in solution:
                while guess in solution:
                    solution.pop(solution.index(guess))
                if len(solution) == 0 and misses < 7:
                    print("You win.")
                    finished = True
            else:
                misses += 1
                if misses == 7 and len(solution) > 0:
                    print("You lose.")
                    finished = True

        if not finished:
            print("You chickened out.")

        round = input()


if __name__ == "__main__":
    main()
