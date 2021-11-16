def is_leap(year):
    leap = False

    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        return True
    else: return False



if __name__ == '__main__':
    year = int(input("Enter a Year: "))
    print(is_leap(year))
    is_leap(year)




