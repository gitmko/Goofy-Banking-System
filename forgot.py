# CustomTKinter as a frontend, Pillow for images
import customtkinter as ctk
from PIL import Image
# JSON for data
import json

# Forgot Password
class ForgotWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("350x300")
        self.title("Goofy Banking App (Forgot Password)")
