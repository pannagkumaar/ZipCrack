import zipfile
import argparse

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except Exception as e:
        return False

def brute_force_zip(zip_file, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            password = line.strip()
            if extract_zip(zip_file, password):
                print(f"Password found: {password}")
                return
    print("Password not found.")

def main():
    parser = argparse.ArgumentParser(description="Zip file brute-force cracker")
    parser.add_argument("-f", "--zipfile", required=True, help="Path to the zip file")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    args = parser.parse_args()

    try:
        zip_file = zipfile.ZipFile(args.zipfile)
    except Exception as e:
        print(f"Failed to open the zip file: {e}")
        return

    brute_force_zip(zip_file, args.wordlist)

if __name__ == "__main__":
    main()
