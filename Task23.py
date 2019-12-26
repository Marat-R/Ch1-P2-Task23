year = int(input("Укажите год: "))

def year_define(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print(f"{year} - не високосный год")
    else:
        print(f"{year} - високосный год")

    # if year % 4 != 0:
    #     print(f"{year} - не високосный год")
    # elif year % 100 == 0:
    #     if year % 400 == 0:
    #         print(f"{year} - високосный год")
    #     else:
    #         print(f"{year} - не високосный год")
    # else:
    #     print(f"{year} - високосный год")

year_define(year)
