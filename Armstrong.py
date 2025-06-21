# Task 8: Armstrong Number Check

def check_armstrong():
    num = int(input("Enter a number: "))
    digits = str(num)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power  # each digit raised to 'power'

    if total == num:
        print(num, "is an Armstrong number!")
    else:
        print(num, "is NOT an Armstrong number.")

# Call the function
check_armstrong()
