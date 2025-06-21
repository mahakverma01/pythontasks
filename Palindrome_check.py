# Task 6: Palindrome Check

def check_palindrome():
    text = input("Enter a word: ")
    
    if text == text[::-1]:  # compare original with reversed
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")

# Call the function
check_palindrome()
