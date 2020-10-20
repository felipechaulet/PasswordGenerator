import string
import pyperclip
from tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, X, Y, BooleanVar, StringVar, Menu
from tkinter.ttk import Frame, Button, Style, Label, Checkbutton
from secrets import choice


class Application(Frame):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.master.title("Password Generator")
        self.style = Style()
        self.style.theme_use("aqua")

        THEMES = [
            ("Alt", "alt"),
            ("Aqua", "aqua"),
            ("Clam", "clam"),
            ("Classic", "classic"),
            ("Default", "default")
        ]

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar)
        file_menu.add_command(label="Exit", command=self.master.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        preferences_menu = Menu(menubar)
        menubar.add_cascade(label="Preferences", menu=preferences_menu)
        themes_menu = Menu(menubar)
        preferences_menu.add_cascade(label="Theme", menu=themes_menu)

        selected_theme = StringVar()
        selected_theme.set("default")
        for name, theme in THEMES:
            selected_theme.set(theme)
            themes_menu.add_radiobutton(label=name, variable=selected_theme, value=theme, command=lambda: self.change_theme(selected_theme.get()))

        ########## Options Panel ##########

        frame_options = Frame(self, relief=RAISED, borderwidth=3)
        frame_options.pack(fill=BOTH, expand=False)

        options_label = Label(frame_options, text="Options:", font=("Arial bold", 16))
        options_label.pack(fill=BOTH, expand=False)

        frame_opt_line1 = Frame(frame_options, borderwidth=0)
        frame_opt_line1.pack(fill=X, expand=True)

        self.has_lower_case = BooleanVar(value=True)
        lower_case_check = Checkbutton(frame_opt_line1, text="Lower Case Characters", variable=self.has_lower_case)
        lower_case_check.pack(side=LEFT, pady=5)

        self.has_upper_case = BooleanVar(value=True)
        upper_case_check = Checkbutton(frame_opt_line1, text="Upper Case Characters", variable=self.has_upper_case)
        upper_case_check.pack(side=LEFT, pady=5, padx=20)

        frame_opt_line2 = Frame(frame_options, borderwidth=0)
        frame_opt_line2.pack(fill=X, expand=True)

        self.has_digits = BooleanVar(value=True)
        digits_check = Checkbutton(frame_opt_line2, text="Numbers", variable=self.has_digits)
        digits_check.pack(side=LEFT, pady=5)

        self.has_special_chars = BooleanVar(value=True)
        special_chars_check = Checkbutton(frame_opt_line2, text="Special Characters", variable=self.has_special_chars)
        special_chars_check.pack(side=LEFT, pady=5, padx=107)

        frame_size = Frame(frame_options, borderwidth=0)
        frame_size.pack(fill=X, expand=True)

        size_label = Label(frame_size, text="Size:", font=("Arial bold", 16))
        size_label.pack(side=LEFT, pady=15)

        self.size = StringVar(value="12")

        minus_button = Button(frame_size, text="-", command=self.decrease_size)
        minus_button.pack(side=LEFT, padx=10)

        size_value = Label(frame_size, textvariable=self.size, font=("Arial bold", 16))
        size_value.pack(side=LEFT, padx=10)

        plus_button = Button(frame_size, text="+", command=self.increase_size)
        plus_button.pack(side=LEFT, padx=10)

        ########## Generate Button Panel ##########

        frame_gen_button = Frame(self, relief=RAISED, borderwidth=0)
        frame_gen_button.pack(fill=BOTH, expand=False)

        generate_pwd_button = Button(frame_gen_button, text="Generate Password", command=self.generate_password)
        generate_pwd_button.pack(fill=None, expand=False)


        ########## Generate Button Panel ##########

        frame_result = Frame(self, relief=RAISED, borderwidth=3)
        frame_result.pack(fill=BOTH, expand=True)

        result_label = Label(frame_result, text="Password:", font=("Arial bold", 16))
        result_label.pack(fill=BOTH, expand=True)

        self.generated_password = StringVar(value="")
        value_label = Label(frame_result, textvariable=self.generated_password, font=("Arial bold", 40), foreground="Blue")
        value_label.pack(fill=Y, expand=True)


        ########## Bottom Button Panel ##########
        self.pack(fill=BOTH, expand=True)

        copy_button = Button(self, text="Copy password to clipboard", command=self.copy_to_clipboard)
        copy_button.pack(side=LEFT)

        close_button = Button(self, text="Close", command=self.master.destroy)
        close_button.pack(side=RIGHT, padx=5, pady=5)

    def increase_size(self):
        current_size = int(self.size.get())
        increased_size = current_size + 1
        self.size.set(str(increased_size))

    def decrease_size(self):
        current_size = int(self.size.get())
        decreased_size = current_size - 1
        self.size.set(str(decreased_size))

    def copy_to_clipboard(self):
        if str(self.generated_password.get()):
            pyperclip.copy(self.generated_password.get())

    def generate_password(self):
        size = int(self.size.get())
        alphabet = ""

        if self.has_lower_case.get():
            alphabet = alphabet + string.ascii_lowercase
        if self.has_upper_case.get():
            alphabet = alphabet + string.ascii_uppercase
        if self.has_digits.get():
            alphabet = alphabet + string.digits
        if self.has_special_chars.get():
            alphabet = alphabet + string.punctuation

        generated_pwd = ''.join([choice(alphabet) for i in range(size)])
        self.generated_password.set(generated_pwd)

    def change_theme(self, theme):
        self.style.theme_use(theme)



def main():
    root = Tk()
    root.geometry("500x300+300+300")
    app = Application()
    root.mainloop()


if __name__ == '__main__':
    main()
