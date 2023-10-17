import customtkinter as ctk
from PIL import Image
# JSON for data
import json

# The window after we log in      
class MainWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Goofy Banking App (Logged In)")
        
        self.label = ctk.CTkLabel(self, text="MainWindow")
        self.label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
