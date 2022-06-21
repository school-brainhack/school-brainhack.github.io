def encrypt_letter(msg, key):
    enc_id = (ord(msg) + ord(key)) % 1114112
    return chr(enc_id)


def decrypt_letter(msg, key):
    dec_id = (1114112 + ord(msg) - ord(key)) % 1114112
    return chr(dec_id)


def process_message(message, key, encrypt):
    returned_message = ""

    for i, letter in enumerate(message):
        if encrypt:
            returned_message += encrypt_letter(letter, key[i%len(key)])
        else:
            returned_message += decrypt_letter(letter, key[i%len(key)])

    return returned_message
