# Task 4: Fibonacci Sequence

def generate_fibonacci():
    n = int(input("Enter how many Fibonacci numbers you want: "))
    
    a, b = 0, 1  # First two numbers
    count = 0

    if n <= 0:
        print("Please enter a positive number.")
    elif n == 1:
        print("Fibonacci sequence: ", a)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(a, end=" ")  # print current number
            a, b = b, a + b    # update values
            count += 1

# Call the function
generate_fibonacci()
