def encrypt_letter(letter, key):
    letter_index = ord(letter)
    key_index = ord(key)
    new_index = (letter_index + key_index) % 1114112
    return chr(new_index)


def decrypt_letter(letter, key):
    letter_index = ord(letter)
    key_index = ord(key)
    new_index = (letter_index - key_index) % 1114112
    return chr(new_index)


def process_message(message, key, encrypt):
    processed_message = ""
    process_letter = encrypt_letter if encrypt else decrypt_letter
    for i, letter in enumerate(message):
        key_letter = key[i % len(key)]
        processed_key = process_letter(letter, key_letter)
        processed_message += processed_key

    return processed_message


if __name__ == "__main__":
    # Test 1
    test_letter = "l"
    test_key = "h"
    decrypted_letter = decrypt_letter(encrypt_letter(test_letter, test_key), test_key)

    if test_letter == decrypted_letter:
        print("first test passed")
    else:
        print("first test failed")

    # Test 2
    message = "word"
    key = "key"

    encrypted_msg = process_message(message, key, encrypt=True)
    decrypted_msg = process_message(encrypted_msg, key, encrypt=False)

    if decrypted_msg == message:
        print("second test passed")
    else:
        print("second test failed")
