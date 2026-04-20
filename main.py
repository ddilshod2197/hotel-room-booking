def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - 97
            result += caesar_encrypt(char, shift)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - 97
            result += caesar_decrypt(char, shift)
            key_index += 1
        else:
            result += char
    return result

text = "Hello, World!"
shift = 3
key = "secret"

encrypted_text = caesar_encrypt(text, shift)
print(f"Caesar encrypted text: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, shift)
print(f"Caesar decrypted text: {decrypted_text}")

vigenere_encrypted_text = vigenere_encrypt(text, key)
print(f"Vigenere encrypted text: {vigenere_encrypted_text}")

vigenere_decrypted_text = vigenere_decrypt(vigenere_encrypted_text, key)
print(f"Vigenere decrypted text: {vigenere_decrypted_text}")
