# CustomTKinter as a frontend, Pillow for images
import customtkinter as ctk
from PIL import Image
# JSON for data
import json

# Registering 
class RegisterWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("350x300")
        self.title("Goofy Banking App (Registering)")

        # Function for registering 
        self.reg_label = ctk.CTkLabel(master=self, text="")
        self.reg_label.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
        self.reg_label_font = ctk.CTkFont(family="Helvetica", size=12)
        self.reg_label.configure(font=self.reg_label_font)

        def save_to_json(details_dict, filename):
            with open(filename, 'a') as file:
                json.dump(details_dict, file)

        def register():
            # Text that shows up on screen
            if len(self.username_entry.get()) == 0 and len(self.password_entry.get()) == 0: 
                self.reg_label.configure(text="The fields are empty")
            elif len(self.username_entry.get()) >= 1 and len(self.password_entry.get()) == 0:
                self.reg_label.configure(text="Something's wrong with your entry")
            elif len(self.password_entry.get()) >= 1 and len(self.username_entry.get()) == 0:
                self.reg_label.configure(text="Something's wrong with your entry")
            elif len(self.username_entry.get()) >= 1 or len(self.password_entry.get()) >= 1:
                self.reg_label.configure(text="Successfully registered!")

            # Creating the dictonary used to store data
            details_dict = {}

            # Saving input to a .json file
            user = self.username_entry.get()
            passw = self.password_entry.get()
            if user:
                details_dict["username"] = user
                details_dict["password"] = passw
                save_to_json(details_dict, "data.json")

                self.username_entry.delete(0, "end")
                self.password_entry.delete(0, "end") # Clear the widgets after we're done
    
        # Text and buttons
        self.register_text = ctk.CTkLabel(master=self, text="Register")
        self.register_text.place(relx=0.28, rely=0.2, anchor=ctk.CENTER)
        self.register_text_font = ctk.CTkFont(family="Helvetica", size=12)
        self.register_text.configure(font=self.register_text_font)

        self.username_entry = ctk.CTkEntry(master=self, width=200, placeholder_text="Username")
        self.username_entry.place(relx=0.5, rely=0.30, anchor=ctk.CENTER)        
        
        self.password_entry = ctk.CTkEntry(master=self, width=200, placeholder_text="Password")
        self.password_entry.place(relx=0.5, rely=0.41, anchor=ctk.CENTER)        
        
        self.register_button = ctk.CTkButton(master=self, width=200, text="Register", command=register)
        self.register_button.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
