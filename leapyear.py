#Write a program to check whether a year is leap year

year = int(input("Enter your prefered year:"))

#divided bt 100 means century year (ending with 00)
#century year divided by 400 is leap year
if (year %400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".fomat(year))
    
#not divided by 100 means not a century year
#year divided by 4 is a leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else :
    print("{0} is not a leap year".format(year))
    