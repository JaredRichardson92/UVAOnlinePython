from math import ceil


def main():
    pages = int(input())
    while pages != 0:
        print("Printing order for {} pages:".format(pages))
        sheets = ceil(pages / 4)
        endPage = sheets * 4
        startPage = 1
        for sheet in range(sheets):
            if endPage > pages:
                spot1 = "Blank"
            else:
                spot1 = endPage

            endPage -= 1

            spot2 = startPage
            startPage += 1
            print("Sheet {}, front: {}, {}".format(sheet + 1, spot1, spot2))

            if pages == 1:
                break
            spot3 = startPage
            startPage += 1

            if endPage > pages:
                spot4 = "Blank"
            else:
                spot4 = endPage

            endPage -= 1
            print("Sheet {}, back : {}, {}".format(sheet + 1, spot3, spot4))

        pages = int(input())


if __name__ == "__main__":
    main()
