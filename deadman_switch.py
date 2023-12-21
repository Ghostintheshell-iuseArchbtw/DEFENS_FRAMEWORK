#Module to be imported to operate the Deadmans Switch.

import argparse
import datetime
import time
import gzip
import logging
import os
import getpass
from cryptography.fernet import Fernet

def decrypt_data(file_path, cipher):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
    
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def decompress_data(file_path):
    with open(file_path, 'rb') as file:
        compressed_data = file.read()
    
    decompressed_data = gzip.decompress(compressed_data)
    
    with open(file_path, 'wb') as file:
        file.write(decompressed_data)

def decrypt_files_and_directories(directory_path, cipher):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_data(file_path, cipher)
            # Assuming shred_file is a function you've defined
            # shred_file(file_path)

def check_passphrase(passphrase, file_path, key_file_path, cipher):
    user_input = getpass.getpass("Enter passphrase: ")
    if user_input == passphrase:
        # Assuming encrypt_and_shred_self is a function you've defined
        # encrypt_and_shred_self(file_path, cipher)
        # shred_file(file_path)
        # delete_file(key_file_path)
        logging.info("System actions avoided for 48 hours. Thank you Dr. Falken.")

def generate_random_passphrase(passphrase_file):
    passphrase = "random_passphrase"
    with open(passphrase_file, 'w') as file:
        file.write(passphrase)

def main():
    parser = argparse.ArgumentParser(description='Encrypt, compress, and shred files and directories.')
    parser.add_argument('file_paths', type=str, nargs='+', help='Paths to the files or directories to encrypt, compress, and shred')
    parser.add_argument('key_file_path', type=str, help='Path to the encryption key file')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the files or directories instead of encrypting, compressing, and shredding')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    parser.add_argument('--interval', type=int, default=24, help='Interval in hours to check for the passphrase (default: 24)')
    parser.add_argument('--passphrase', type=str, default='200OK', help='Passphrase to trigger the actions (default: 200OK)')
    parser.add_argument('--generate-passphrase', action='store_true', help='Generate a random passphrase and save it to a file')
    parser.add_argument('--passphrase-file', type=str, default='passphrase.txt', help='Path to the passphrase file (default: passphrase.txt)')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # This assumes read_key_from_file is a function you've defined
        encryption_key = read_key_from_file(args.key_file_path)
    except FileNotFoundError:
        logging.error(f"Encryption key file not found: {args.key_file_path}")
        return

    cipher = Fernet(encryption_key)

    if args.generate_passphrase:
        generate_random_passphrase(args.passphrase_file)
        logging.info(f"Passphrase generated and saved to {args.passphrase_file}")
        return

    if args.decrypt:
        for file_path in args.file_paths:
            if os.path.isfile(file_path):
                try:
                    decrypt_data(file_path, cipher)
                    decompress_data(file_path)
                except FileNotFoundError:
                    logging.error(f"File not found: {file_path}")
            elif os.path.isdir(file_path):
                try:
                    decrypt_files_and_directories(file_path, cipher)
                    # Assuming delete_empty_directories is a function you've defined
                    # delete_empty_directories(file_path)
                except FileNotFoundError:
                    logging.error(f"Directory not found: {file_path}")
            else:
                logging.error(f"Invalid file or directory path: {file_path}")
    else:
        for file_path in args.file_paths:
            if os.path.isfile(file_path):
                try:
                    # Assuming compress_file is a function you've defined
                    # compress_file(file_path)
                    # encrypt_and_shred_file(file_path, cipher)
                    # shred_file(file_path)
                except FileNotFoundError:
                    logging.error(f"File not found: {file_path}")
            elif os.path.isdir(file_path):
                try:
                    # Assuming encrypt_compress_and_shred_directory is a function you've defined
                    # encrypt_compress_and_shred_directory(file_path, cipher)
                    # delete_empty_directories(file_path)
                except FileNotFoundError:
                    logging.error(f"Directory not found: {file_path}")
            else:
                logging.error(f"Invalid file or directory path: {file_path}")

    while True:
        for file_path in args.file_paths:
            try:
                check_passphrase(args.passphrase, file_path, args.key_file_path, cipher)
            except FileNotFoundError:
                logging.error(f"File not found: {file_path}")
        logging.info(f"Waiting for {args.interval} hours...")
        time.sleep(args.interval * 3600)

if __name__ == "__main__":
    main()


