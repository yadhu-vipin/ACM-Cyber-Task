import pyzipper
import os

zip_file_path = '/home/yadhu_vipin/Downloads/Trybreakingme.zip'
output_dir = '/home/yadhu_vipin/Downloads/Trybreakingme_extracted/'
wordlist_path = '/home/yadhu_vipin/Downloads/rockyou.txt'

def brute_force_zip_password(zip_file, wordlist):
    if not os.path.exists(zip_file):
        print(f"ZIP file not found at: {zip_file}")
        return None

    if not os.path.exists(wordlist):
        print(f"Wordlist file not found at: {wordlist}")
        return None

    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

    try:
        with open(wordlist, 'r', encoding='latin-1') as file:
            for line in file:
                password = line.strip()
                try:
                    with pyzipper.AESZipFile(zip_file) as zf:
                        zf.pwd = password.encode('utf-8')
                        zf.extractall(output_dir)
                        print(f"Password found: {password}")
                        return password
                except (RuntimeError, pyzipper.BadZipFile):
                    continue
                except Exception as e:
                    print(f"An error occurred during extraction: {e}")

        print("Password not found.")
        return None
    except Exception as e:
        print(f"An error occurred while opening the wordlist: {e}")
        return None

brute_force_zip_password(zip_file_path, wordlist_path)
