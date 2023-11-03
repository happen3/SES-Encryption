def encrypt(input_string, key):
    encrypted_string = ""
    for char in input_string:
        encrypted_char = chr((ord(char) + key) % 128)  # Use modulo to wrap around ASCII characters
        encrypted_string += encrypted_char
    return encrypted_string

def decrypt(encrypted_string, key):
    decrypted_string = ""
    for char in encrypted_string:
        decrypted_char = chr((ord(char) - key) % 128)  # Use modulo to wrap around ASCII characters
        decrypted_string += decrypted_char
    return decrypted_string
