#!/usr/bin/env python
import argparse
import os
from useful_functions import encrypt_letter, decrypt_letter, process_message

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str, help="Path to the text file containing the message \
                        to be encrypted or decrypted.")
    parser.add_argument("--key", type=str, help="Key to use to encrypt or decrypt the message.")
    parser.add_argument("--mode", type=str, choices=["enc", "dec"], help="Wether to encrypt ('enc') \
                        or decrypt ('dec') the message.")
    args = parser.parse_args()

    with open(args.message, 'r') as f:
        message = f.read()
    encrypt = args.mode == "enc"
    processed_message = process_message(message, args.key, encrypt)
    suffix = "_encrypted" if encrypt else "_decrypted"
    save_path = os.path.splitext(args.message)[0] + suffix + ".txt"
    with open(save_path, 'w') as f:
        f.write(processed_message)
