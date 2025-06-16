# Cypher is 15th letter after the letter used. 
# Plain  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Cypher P Q R S T U V W X Y Z A B C D E F G H I J K L M N O

# Cypher is 15th number after number used.
# Plain  0 1 2 3 4 5 6 7 8 9
# Cypher 5 6 7 8 9 0 1 2 3 4

def encode(message, shift):
    
    '''In the char.islower() and char.isupper() if statements each 
    character in the input message will be iterated over and:
    1. Char will be converted to unicode value using ord() function.
    2. Char index in range 0-25 will be calculated by subtracting
       ord('a') or ord('A').
    3. Positive shift will be performed using modulo operation.
    4. Char will be converted to a new character by adding 
       ord('a') or ord('A').
    '''

    # Empty string for input message.
    enc_message = ""

    # Loop through all the characters in the input message.
    for char in message:
        # If character is a lowercase letter it is encoded and added to 
        # enc_message.
        if char.islower():
            # chr() function to return the corresponding character of the 
            # unicode value.
            enc_message += chr(((ord(char) - ord('a')) + shift) % 26 + ord('a'))
        
        # If character is an uppercase letter it is encoded and added to
        # enc_message. 
        elif char.isupper():
            enc_message += chr(((ord(char) - ord('A')) + shift) % 26 + ord('A'))

        # If character is a number it is encoded and added to enc_message.
        elif char.isdigit():
            # Integer shifted and converted to string value.
            enc_message += str((int(char) + shift) % 10)

        # If character is not a letter or number nothing is done to it.
        else:
            enc_message += char

    return enc_message

# User inputs message.
input_message = input("Enter a message: ")

# Call the encode function.
encoded_message = encode(input_message, 15)

# Print the input message and the encoded message.
print(f'''Input message: "{input_message}"  
Encoded message: "{encoded_message}"''')

# References:
# I used https://www.geeksforgeeks.org/ascii-table/
# to help understand the ASCII values of characters.
# I used https://likegeeks.com/python-caesar-cipher/ to help understand the 
# ord() and chr() functions.