import argparse
from cryptography.fernet import Fernet

## Usage: python -u decrypt.py -k "98_-qPEPd_r_jSadzmo3tywzbFn5e9GcwMjzsj99wig=" -m "gAAAAABlk9TV_kZntym_8fNN83EbIJL1X3KxkZCNYLJZF_RtVQykDfcyNUq3V0iTu7RhYwRkJjsupBEY6bItogiy6ljBDQy1eA=="
    
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', required=True)
    parser.add_argument('-m', '--message', required=True)
    args = parser.parse_args()

    print("Key: ", type(args.key))
    print("Message: ", args.message)

    key = bytes(args.key, 'utf-8')

    fernet = Fernet(key)

    encMessage = args.message.encode('utf-8')

    print("Encrypted string: ", encMessage)

    decMessage = fernet.decrypt(encMessage).decode()

    print("Decrypted string: ", decMessage)


if __name__ == "__main__":
    main()
