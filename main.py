# CustomTKinter as a frontend, Pillow for images
import customtkinter as ctk
from PIL import Image
# JSON for data
import json
# Importing classes
from forgot import ForgotWindow
from register import RegisterWindow
from window import MainWindow

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# The starting app
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x600")
        self.title("Goofy Banking App")
        
        # Logo
        logo = ctk.CTkImage(light_image=Image.open("./images/logo.png"),
                                          size=(100, 100))
        logo_label = ctk.CTkLabel(master=self, image=logo, text="")  # display image with a CTkLabel
        logo_label.place(relx=0.38, rely=0.03)
        
        logo_text = ctk.CTkLabel(master=self, text="[ Goofy Banking App™ ]")
        logo_text.place(relx=0.5, rely=0.23, anchor=ctk.CENTER)
        logo_text_font = ctk.CTkFont(family="Helvetica", size=22)
        logo_text.configure(font=logo_text_font)
        
        # Logging in
        login_text = ctk.CTkLabel(master=self, text="Login")
        login_text.place(relx=0.29, rely=0.32, anchor=ctk.CENTER)
        login_text_font = ctk.CTkFont(family="Helvetica", size=12)
        login_text.configure(font=login_text_font)
        
        user_entry = ctk.CTkEntry(master=self, width=200, placeholder_text="Username")
        user_entry.place(relx=0.5, rely=0.37, anchor=ctk.CENTER)
        
        pass_entry = ctk.CTkEntry(master=self, width=200, placeholder_text="Password")
        pass_entry.place(relx=0.5, rely=0.43, anchor=ctk.CENTER)
        
        login_button = ctk.CTkButton(master=self, width=200, text="Login", command=self.open_login)
        login_button.place(relx=0.5, rely=0.50, anchor=ctk.CENTER)
        
        # Registering
        register_text = ctk.CTkLabel(master=self, text="Don't have an account?")
        register_text.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
        register_text_font = ctk.CTkFont(family="Helvetica", size=14)
        register_text.configure(font=register_text_font)
        
        register_button = ctk.CTkButton(master=self, text="Register", command=self.open_register)
        register_button.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)
        
        # Forgot password
        forgot_pass_text = ctk.CTkLabel(master=self, text="Forgot your password?")
        forgot_pass_text.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)
        forgot_pass_text_font = ctk.CTkFont(family="Helvetica", size=14)
        forgot_pass_text.configure(font=forgot_pass_text_font)
        
        forgot_pass_button = ctk.CTkButton(master=self, text="Reset password", command=self.open_fp)
        forgot_pass_button.place(relx=0.5, rely=0.80, anchor=ctk.CENTER)
    
        self.register_window = None
        self.login_window = None
        self.fp_window = None

    def open_register(self):
        if self.register_window is None or not self.register_window.winfo_exists():
            self.register_window = RegisterWindow(self)
        else:
            self.register_window.focus()
        
    def open_login(self):
        if self.login_window is None or not self.login_window.winfo_exists():
            self.login_window = MainWindow(self)
        else:
            self.login_window.focus()
            
    def open_fp(self):
        if self.fp_window is None or not self.fp_window.winfo_exists():
            self.fp_window = ForgotWindow(self)
        else:
            self.fp_window.focus()

app = App()
app.mainloop()