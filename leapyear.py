year=2800

#write a function to check if given year is leap year or not
def is_leap(year):
    leap = False
    
    # Constraints: 1000 <= year <= 10**5
    if year < 1000 or year > 10**5:
        print("Year out of range")
    # If the year can be divided by 4 evenly (%4==0) unless
    else: 
        if year % 4 == 0:
            leap = True
    # If the year can be divided by 100 but not by 400, it is not a leap year unless
        elif year % 100 == 0 and year % 400 != 0:
            leap = False
    # If the year is also evenly divisible by 400, then it is a leap year
        elif year % 400 == 0:
            leap = True

    return leap

#call function with a value
gregorianyear = is_leap(2025)
print(gregorianyear)