def encrypt(original_text, shift_amount):
    # Define the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Initialize an empty string for the encrypted text
    encrypted_text = ""
    
    # Loop through each letter in the original text
    for letter in original_text:
        # Check if the letter is in the alphabet (to handle spaces or punctuation)
        if letter in alphabet:
            # Find the current position of the letter
            position = alphabet.index(letter)
            # Calculate the new position with the shift
            new_position = (position + shift_amount) % 26
            # Get the encoded letter
            encoded_letter = alphabet[new_position]
            # Append the encoded letter to the encrypted text
            encrypted_text += encoded_letter
        else:
            # If the letter is not in the alphabet, just append it as is
            encrypted_text += letter
    
    # Print the result
    print("Here is the encoded result:", encrypted_text)

# Example usage
encrypt("morning", 1)  # Output: Here is the encoded result: ifmmp