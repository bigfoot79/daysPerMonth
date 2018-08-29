
def daysPerMonth(year, month):

    # Days per month is statis for all months except February
    if(month in [1,3,5,7,8,10,12]):
        return(31)
    elif(month in [4,6,9,11]):
        return(30)
    else:
        # Days per month in February will vary depending upon leap year
        # Every 400 years is a leap year (starting at year 0)
        # Every 100 years is NOT a leap year (starting at year 0)
        # Every 4th year is a leap year (starting at year 0)
        # Every other year is NOT a leap year (starting at year 0)

        if(year % 400 == 0):
            return(29)
        elif(year % 100 == 0):
            return(28)
        elif(year % 4 == 0):
            return(29)
        else:
            return(28)


def main():

    month = 2
    year = 2100
    daysPerMonth_result = daysPerMonth(year,month)
    print(daysPerMonth_result)


if __name__ == '__main__':

    main()
