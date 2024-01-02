import argparse
from cryptography.fernet import Fernet

## Usage: python -u encrypt.py "encrypt this message"


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("message")
    args = parser.parse_args()

    message = args.message
    
    key = Fernet.generate_key()
    print("Key: ", key)

    print("Original Message: ", message)
    
    fernet = Fernet(key)
    
    encMessage = fernet.encrypt(message.encode())
    print("Encrypted String: ", encMessage)

if __name__ == "__main__":
    main()
