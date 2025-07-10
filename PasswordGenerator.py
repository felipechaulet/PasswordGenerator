import string
import pyperclip
import customtkinter as ctk
from secrets import choice


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Password Generator")
        self.geometry("500x520")
        self.resizable(False, False)
        
        # Set theme
        ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
        
        self.init_ui()

    def init_ui(self):
        # Create main container
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(main_frame, text="Password Generator", 
                                  font=ctk.CTkFont(size=24, weight="bold"))
        title_label.pack(pady=(20, 30))
        
        # Create menu bar
        self.create_menu()

        # Options Panel - Minimalist
        options_frame = ctk.CTkFrame(main_frame)
        options_frame.pack(fill="x", padx=20, pady=(0, 30))
        
        # Options title
        ctk.CTkLabel(options_frame, text="⚙️ Options", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(15, 10))
        
        # Single row checkbox layout
        checkbox_container = ctk.CTkFrame(options_frame, fg_color="transparent")
        checkbox_container.pack(pady=(0, 20), expand=True)
        
        self.has_lower_case = ctk.BooleanVar(value=True)
        lower_case_check = ctk.CTkCheckBox(checkbox_container, text="abc", variable=self.has_lower_case)
        lower_case_check.pack(side="left", padx=8, expand=True)
        
        self.has_upper_case = ctk.BooleanVar(value=True)
        upper_case_check = ctk.CTkCheckBox(checkbox_container, text="ABC", variable=self.has_upper_case)
        upper_case_check.pack(side="left", padx=8, expand=True)
        
        self.has_digits = ctk.BooleanVar(value=True)
        digits_check = ctk.CTkCheckBox(checkbox_container, text="123", variable=self.has_digits)
        digits_check.pack(side="left", padx=8, expand=True)
        
        self.has_special_chars = ctk.BooleanVar(value=True)
        special_chars_check = ctk.CTkCheckBox(checkbox_container, text="!@#", variable=self.has_special_chars)
        special_chars_check.pack(side="left", padx=8, expand=True)

        # Password length slider
        length_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        length_frame.pack(fill="x", padx=20, pady=(10, 20))
        
        ctk.CTkLabel(length_frame, text="Password Length:", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        
        self.length_var = ctk.IntVar(value=12)
        self.length_label = ctk.CTkLabel(length_frame, text="12", font=ctk.CTkFont(size=14, weight="bold"))
        self.length_label.pack(side="right", padx=(10, 0))
        
        self.length_slider = ctk.CTkSlider(length_frame, from_=4, to=30, number_of_steps=26,
                                          variable=self.length_var, command=self.update_length_label)
        self.length_slider.pack(side="right", padx=(10, 10), fill="x", expand=True)
        
        # Password Display
        result_frame = ctk.CTkFrame(main_frame)
        result_frame.pack(fill="x", padx=20, pady=(20, 20))
        
        ctk.CTkLabel(result_frame, text="Generated Password:", 
                    font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(15, 5))
        
        self.password_entry = ctk.CTkEntry(result_frame, font=ctk.CTkFont(size=16), 
                                          height=40, justify="center")
        self.password_entry.pack(fill="x", padx=20, pady=(0, 15))
        
        # Bottom Buttons - All in one line
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Center the buttons
        center_frame = ctk.CTkFrame(button_frame, fg_color="transparent")
        center_frame.pack(expand=True)
        
        generate_button = ctk.CTkButton(center_frame, text="🔄", 
                                       font=ctk.CTkFont(size=18),
                                       width=50, height=50, corner_radius=25,
                                       command=self.generate_password)
        generate_button.pack(side="left", padx=10)
        
        copy_button = ctk.CTkButton(center_frame, text="📋", 
                                   font=ctk.CTkFont(size=18),
                                   command=self.copy_to_clipboard, 
                                   width=50, height=50, corner_radius=25)
        copy_button.pack(side="left", padx=10)
        
        close_button = ctk.CTkButton(center_frame, text="✕", 
                                    font=ctk.CTkFont(size=18),
                                    command=self.destroy, 
                                    width=50, height=50, corner_radius=25,
                                    fg_color="red", hover_color="darkred")
        close_button.pack(side="left", padx=10)

    def create_menu(self):
        import tkinter as tk
        # Create menu bar using tkinter
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Generate Password", command=self.generate_password)
        file_menu.add_command(label="Copy to Clipboard", command=self.copy_to_clipboard)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.destroy)
        
        # View menu for theme
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        
        self.theme_var = tk.StringVar(value="dark")
        view_menu.add_radiobutton(label="Light Theme", variable=self.theme_var, 
                                 value="light", command=lambda: self.change_theme("light"))
        view_menu.add_radiobutton(label="Dark Theme", variable=self.theme_var, 
                                 value="dark", command=lambda: self.change_theme("dark"))
        view_menu.add_radiobutton(label="System Theme", variable=self.theme_var, 
                                 value="system", command=lambda: self.change_theme("system"))

    def update_length_label(self, value):
        self.length_label.configure(text=str(int(value)))

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)

    def generate_password(self):
        size = int(self.length_var.get())
        alphabet = ""

        if self.has_lower_case.get():
            alphabet += string.ascii_lowercase
        if self.has_upper_case.get():
            alphabet += string.ascii_uppercase
        if self.has_digits.get():
            alphabet += string.digits
        if self.has_special_chars.get():
            alphabet += string.punctuation

        if not alphabet:
            alphabet = string.ascii_letters + string.digits  # Fallback

        generated_pwd = ''.join([choice(alphabet) for _ in range(size)])
        self.password_entry.delete(0, 'end')
        self.password_entry.insert(0, generated_pwd)

    def change_theme(self, theme):
        ctk.set_appearance_mode(theme)



def main():
    app = Application()
    app.mainloop()


if __name__ == '__main__':
    main()
