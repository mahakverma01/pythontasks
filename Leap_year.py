# Task 7: Leap Year Check

def check_leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year, "is a Leap Year!")
    else:
        print(year, "is NOT a Leap Year.")

# Call the function
check_leap_year()
