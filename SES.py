# The SES (simple encryption system) Encryption system

import MixList
import hashlib
import math
import xor

class InvalidKeyError(Exception):
    def __init__(self, message="Invalid key value, must not be 0 nor a negative integer!"):
        self.message = message
        super().__init__(self.message)

class InvalidIterationCount(Exception):
    def __init__(self, message="Invalid interation count, must not be 1 or more and not a negative integer!"):
        self.message = message
        super().__init__(self.message)



def encrypt(in_str, key: int, iterations: int = 10, iv: int = 123456789):

    if key == 0:
        raise(InvalidKeyError)
    
    # Initialize the key derivation function (KDF) using SHA224.
    kdf = hashlib.sha224()
    FES = MixList.encrypt(in_str, key)
    FES = MixList.encrypt(in_str, key)
    for _ in range(iterations):
        # Use the KDF to generate a second stage xor key
        kdf.update(str(key * 2240 + iv).encode('utf-8'))
        # Apply the second stage encryption
        FES = xor.xor(FES, str(math.floor(iv * 96 / 3 * 0.5 * key)))
        FES = xor.xor(FES, (str(iv)+kdf.hexdigest()))
    # Return the final encrypted string
    FES = MixList.encrypt(FES, math.floor(iv / key + 30))
    return FES

def decrypt(encrypted_str, key: int, iterations: int = 10, iv: int = 123456789):

    if key == 0:
        raise(InvalidKeyError)
    
    # Initialize the key derivation function (KDF) using SHA224.
    encrypted_str = MixList.decrypt(encrypted_str, math.floor(iv / key + 30))
    kdf = hashlib.sha224()
    for _ in range(iterations):
        # Use the KDF to generate the second stage xor key
        kdf.update(str(key * 2240 + iv).encode('utf-8'))
        # Apply the second stage decryption (XOR operation)
        encrypted_str = xor.xor(encrypted_str, (str(iv)+kdf.hexdigest()))
        encrypted_str = xor.xor(encrypted_str, str(math.floor(iv * 96 / 3 * 0.5)))
    # Reverse the first stage decryption using MixList.decrypt function
    decrypted_str = MixList.decrypt(encrypted_str, key)
    decrypted_str = MixList.decrypt(encrypted_str, key)
    # Return the decrypted string
    return decrypted_str
