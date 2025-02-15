# Customtkineter
import customtkinter as ctk
from customtkinter import CTkLabel, CTkScrollableFrame, CTkButton

# tkinter
import tkinter.font as tkFont
from tkinter import Tk, Label, messagebox, Scrollbar, Canvas, Frame, Toplevel

# System utilities
import os
import sys

# handle_data script
# from handle_data import load_data


print("Starting GUI Setup...") # Console check.
root = ctk.CTk() # Initialise customtkinter window
print("Root window created.") # Console check.

ctk.set_appearance_mode("Light") # Disable the default/autmatic appearance detection with ctk.