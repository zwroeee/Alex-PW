```markdown
# Password Manager

A simple password manager built in Python that allows you to securely store and manage your passwords. The passwords are encrypted for security, and the application provides functionalities to generate, view, add, and delete passwords.

## Features

- **Secure Storage**: Passwords are encrypted using the `cryptography` library.
- **Clipboard Support**: Automatically copy generated passwords to the clipboard.
- **Auto-lock**: Inactivity auto-lock feature to secure your password manager.
- **Category Management**: Organize your passwords into categories.

## Requirements

To run this password manager, you will need:

- **Python 3.x**: Make sure Python 3 is installed on your machine. [Download Python](https://www.python.org/downloads/).
- **Required Libraries**: The following Python libraries are required:
  - `cryptography`: For encrypting and decrypting passwords.
  - `pyperclip`: For managing clipboard operations.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zwroeee/Alexs-pw.git
   cd password-manager
   ```

2. Create a `requirements.txt` file in the root directory of the cloned repository with the following content:
   ```
   cryptography
   pyperclip
   pyinstaller
   ```

3. Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**:
   - Open terminal or command prompt.
   - Execute the following command:
     ```bash
     python password_manager.py
     ```

5. **Configuration**:
   - Set a master password within the script by modifying the `MASTER_PASSWORD` variable.
   - The script will generate a `secret.key` file for encryption upon initial run.

### Usage

- **Add a Password**: Choose the "add" option to enter a website, username, password, and category.
- **View Passwords**: Select "view" to see stored passwords. You can filter by category.
- **Delete a Password**: Choose "delete" to remove passwords from storage.
- **Generate Password**: Use the "generate" option to create a secure random password of your desired length.
- **Exit**: Choose "exit" to close the application.

### Security Note

Ensure the `secret.key` and `passwords.json` files are kept secure and not exposed publicly. Modify permissions as necessary to maintain their confidentiality.

### License

This project is open-source and available under the MIT License.

### Contributing

Feel free to contribute! Open an issue or submit a pull request for any enhancements or bug fixes.

### Acknowledgments

- Thanks to the developers of the `cryptography` and `pyperclip` libraries for their excellent work.
