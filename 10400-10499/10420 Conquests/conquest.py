# 10420


def main():
    names = int(input())
    countries = {}

    for _ in range(names):
        country = input().split()[0]
        if country not in countries.keys():
            countries[country] = 1
        else:
            countries[country] += 1

    countryList = list(countries.keys())

    countryList.sort()

    for country in countryList:
        print(country + " " + str(countries[country]))


if __name__ == "__main__":
    main()
