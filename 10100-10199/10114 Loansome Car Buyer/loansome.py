def loan(dur, downPayment, loanAmount, depPeriods):
    rates = {}
    for i in range(int(depPeriods)):
        month, rate = map(float, input().split())
        for i in range(int(month), 110):
            rates[i] = 1 - rate

    monthlyPayment = loanAmount / dur
    carValue = (loanAmount + downPayment) * rates[0]
    month = 0

    while carValue < loanAmount:
        month += 1
        loanAmount = loanAmount - monthlyPayment
        carValue = carValue * rates[month]

    if month == 1:
        print("1 month")
    else:
        print(str(month) + " months")


def main():
    dur, payment, loanAmount, depPeriods = map(float, input().split())
    while dur > 0:
        loan(dur, payment, loanAmount, depPeriods)
        dur, payment, loanAmount, depPeriods = map(float, input().split())


if __name__ == "__main__": main()
