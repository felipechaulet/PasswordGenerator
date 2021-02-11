# PasswordGenerator

Simple Python Password Generator.

Allows the user to include:

    - Lower case characters
    - Upper case characters
    - Numbers
    - Special characters (such as symbols)
    
Generates a password with the selected options
Has a button to copy the password to the clipboard


Notes:
* Python version used for development: 3.8
* Pyperclip used to copy the password to clipboard (pip install -r requirements.txt)
* Tested on MacOS Catalina and Fedora (Aqua theme not installed by default)

GUI:

![GUI](https://github.com/felipechaulet/PasswordGenerator/blob/master/blob/main_gui.png)


Known issues:
* If the password is bigger than the window size, you won't be able to see the entire password
* Depending on the OS, the default size is not enough to show the interface correctly. Some items might not appear entirely. Resizing the window fixes it