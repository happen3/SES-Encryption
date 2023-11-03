def xor(plaintext, key):
    encrypted_text = ""
    for i in range(len(plaintext)):
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
        encrypted_text += encrypted_char
    return encrypted_text
