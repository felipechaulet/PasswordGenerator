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
* Tested on MacOS Catalina only


Password generation (could use some improvement):
    
    - It generates one password of the defined size for each selected option
    - It contatenates all the generated passwords
    - It shuffles the concatenated password 5 times
    - It cuts the "n" characters of the shuffled password, where "n" is the size of the password
    
This means that even if the user selects one of the options, that doesn't mean the generated password will contain that character.
