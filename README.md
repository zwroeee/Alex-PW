![Capture](https://github.com/user-attachments/assets/0588ed42-3d92-4929-8863-d283d5190227)
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

- **Windows**: This executable is built for Windows. Make sure your system meets the requirements for running `.exe` files.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zwroeee/Alexs-pw.git
   cd password-manager
   ```

2. **Running the Application**:
   - Navigate to the `dist` folder where the `password_manager.exe` file is located.
   - Double-click on `password_manager.exe` to run the application.

3. **Configuration**:
   - Upon initial run, the application will generate a `secret.key` file for encryption.

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
