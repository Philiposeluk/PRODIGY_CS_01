def caesar_cipher(text, shift):
    result = ""
    
    # Iterate through each character in the text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, keep it the same
        else:
            result += char

    return result

def main():
    while True:
        action = input("Would you like to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()
        
        if action == 'q':
            print("Goodbye!")
            break
        
        if action not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (positive for right, negative for left): "))
        
        if action == 'e':
            encrypted_message = caesar_cipher(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif action == 'd':
            decrypted_message = caesar_cipher(message, -shift)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
