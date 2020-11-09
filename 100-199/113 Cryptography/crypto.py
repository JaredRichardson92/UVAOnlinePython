while True:
    try:
        n = int(input().split()[0])
        p = int(input().split()[0])
        # Calculates value, may be too low due to rounding errors
        val = int(p ** (1.0 / n))
        # Checks for case of rounding error and adjusts
        if val ** n == p:
            print(str(val))
        else:
            print(str(val+1))

    # End loop after all input is read.
    except EOFError:
        break
