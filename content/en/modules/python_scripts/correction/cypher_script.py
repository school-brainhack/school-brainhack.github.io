import argparse
from useful_functions import process_message


def main(input_path, key, mode, output_path):
    with open(input_path, "r") as message_file:
        message = message_file.read()
    encrypt = mode == "encryption"
    processed_message = process_message(message, key, encrypt)
    with open(output_path, "w") as out_file:
        out_file.write(processed_message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        dest="input_path",
        type=str,
        required=True,
        help="Path to the input file.",
    )
    parser.add_argument(
        "-o",
        dest="output_path",
        type=str,
        required=True,
        help="Path to the output file.",
    )
    parser.add_argument("-k", dest="key", type=str, required=True, help="Key.")
    parser.add_argument(
        "-m",
        dest="mode",
        type=str,
        required=True,
        choices=["encryption", "decryption"],
        help="Wether to encrypt or decrypt the message.",
    )
    args = parser.parse_args()
    main(args.input_path, args.key, args.mode, args.output_path)
