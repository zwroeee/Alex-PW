import json
import os
import subprocess
import sys
from cryptography.fernet import Fernet
import random
import string
import time
import pyperclip
import threading


def install_requirements():
    """Install required packages from requirements.txt."""
    try:
        # Check if `requirements.txt` exists
        if os.path.exists("requirements.txt"):
            # Install packages listed in `requirements.txt`
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except Exception as e:
        print(f"An error occurred while installing requirements: {e}")


def print_banner():
    banner = r"""
     _____  .__                          __________                                               .___    _____                                             
    /  _  \ |  |   ____ ___  ___  ______ \______   \_____    ______ ________  _  _____________  __| _/   /     \ _____    ____ _____     ____   ___________ 
   /  /_\  \|  | _/ __ \\  \/  / /  ___/  |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |   /  \ /  \\__  \  /    \\__  \   / ___\_/ __ \_  __ \
  /    |    \  |_\  ___/ >    <  \___ \   |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |  /    Y    \/ __ \|   |  \/ __ \_/ /_/  >  ___/|  | \/
  \____|__  /____/\___  >__/\_ \/____  >  |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |  \____|__  (____  /___|  (____  /\___  / \___  >__|   
          \/          \/      \/     \/                  \/     \/     \/                          \/          \/     \/     \/     \//_____/
    """
    print(banner)


# Functionality for key management
def generate_key():
    return Fernet.generate_key()


def load_key():
    return open("secret.key", "rb").read()


# Encryption/Decryption functions
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message


# Save and load passwords feature
def save_password(website, username, password, category):
    encrypted_password = encrypt_message(password)
    data = {website: {'username': username, 'password': encrypted_password.decode(), 'category': category}}

    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            all_data = json.load(file)

        all_data.update(data)
    else:
        all_data = data

    with open("passwords.json", "w") as file:
        json.dump(all_data, file)


def view_passwords(category=None):
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            all_data = json.load(file)
            for website, info in all_data.items():
                decrypted_password = decrypt_message(info['password'].encode())

                # Check if category exists; default to "Uncategorized" if not found
                if 'category' not in info:
                    info['category'] = "Uncategorized"  # Assign a default category

                if category is None or (category and info['category'] == category):
                    print(
                        f"Website: {website}, Username: {info['username']}, Password: {decrypted_password}, Category: {info['category']}")
    else:
        print("No passwords stored.")


def delete_password(website):
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            all_data = json.load(file)

        if website in all_data:
            del all_data[website]
            with open("passwords.json", "w") as file:
                json.dump(all_data, file)
            print(f"Password for website '{website}' has been deleted.")
        else:
            print(f"No password found for website '{website}'.")
    else:
        print("No passwords stored.")


def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for _ in range(length))
    return password


# Auto-lock feature
last_active_time = time.time()


def auto_lock():
    global last_active_time
    while True:
        time.sleep(60)  # Check every minute
        if time.time() - last_active_time > 300:  # 5 minutes
            print("\nSession locked due to inactivity. Please restart the program.")
            os._exit(0)


def reset_timer():
    global last_active_time
    last_active_time = time.time()


# Master password management
MASTER_PASSWORD = "Your master password"  # Secure this


def verify_master_password():
    while True:
        user_input = input("Enter master password to continue: ")
        if user_input == MASTER_PASSWORD:
            print("Access granted.")
            reset_timer()
            break
        else:
            print("Incorrect password. Try again.")


# Clipboard functionality
def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("Copied to clipboard!")


# Migration function to add categories to existing data
def migrate_password_data():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            # Attempt to load JSON data; handle potential errors
            try:
                all_data = json.load(file)
            except json.JSONDecodeError:
                print("Error: passwords.json is corrupted or empty. Initializing a new file.")
                all_data = {}

        # Modify the existing data to add a default category if it doesn't exist
        for website, info in all_data.items():
            if 'category' not in info:
                info['category'] = "Uncategorized"  # Assign a default category

        # Save the modified data back to the file
        with open("passwords.json", "w") as file:
            json.dump(all_data, file)


# Main function
def main():
    install_requirements()  # Install required packages
    # Ensure the secret key exists
    if not os.path.exists("secret.key"):
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    # Initialize empty passwords file if it doesn't exist or is invalid
    if not os.path.exists("passwords.json"):
        with open("passwords.json", "w") as file:
            json.dump({}, file)  # Start with an empty JSON object

    # Migrate existing data to include categories
    migrate_password_data()

    # Start auto-lock thread
    threading.Thread(target=auto_lock, daemon=True).start()

    verify_master_password()  # Require master password on startup

    while True:
        choice = input("Would you like to [add], [view], [delete], [generate], or [exit]? ").lower()
        reset_timer()  # Reset inactivity timer upon any action

        if choice == "add":
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            category = input("Category: ")
            save_password(website, username, password, category)

        elif choice == "view":
            category = input("Enter category to filter by (leave blank for all): ")
            view_passwords(category.strip() if category.strip() else None)

        elif choice == "delete":
            website = input("Enter the website to delete the password for: ")
            delete_password(website)

        elif choice == "generate":
            length = int(input("Password length: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
            copy_to_clipboard(password)  # Automatically copy generated password to clipboard

        elif choice == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    print_banner()  # Print the banner
    main()