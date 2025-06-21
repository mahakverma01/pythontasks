# Task 3: Factorial Calculation

def calculate_factorial():
    num = int(input("Enter a number: "))
    factorial = 1  # Starting value
    
    if num < 0:
        print("Factorial does not exist for negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):  # loop from 1 to num
            factorial *= i  # same as factorial = factorial * i
        print("The factorial of", num, "is", factorial)

# Call the function
calculate_factorial()
