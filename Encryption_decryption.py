# Task 9: Custom Encryption-Decryption (Caesar Cipher)

def encrypt(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():  # only shift alphabets
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char  # keep spaces/symbols as is
    return encrypted


def decrypt(text, key):
    return encrypt(text, -key)  # decryption is reverse shift


def custom_encryption_decryption():
    choice = input("Do you want to Encrypt or Decrypt? (e/d): ").lower()
    message = input("Enter your message: ")
    key = int(input("Enter shift key (e.g., 3): "))

    if choice == 'e':
        result = encrypt(message, key)
        print("Encrypted Message:", result)
    elif choice == 'd':
        result = decrypt(message, key)
        print("Decrypted Message:", result)
    else:
        print("Invalid choice. Enter 'e' or 'd'.")

# Call the function
custom_encryption_decryption()
