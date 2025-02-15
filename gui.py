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

root.update_idletasks()
root.geometry("100+100")
root.deiconify()

# Window positioning (centre dynamically).
width, height = 600, 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# Fonts
univers_font = ("Univers", 16)
geneva_font = ("Geneva", 16)
# Initialising x + y co-ordinates of the mouse drag operation in global scope.
root._drag_start_x = 0
root._drag_start_y = 0
# Creating custom title bar.
def move_window(event):
    root.geometry(f"{width}x{height}+{x}+{y}")

title_bar = ctk.CTkFrame(root, height=30, fg_color="#fbc42c") # Custom Title bar.
title_bar.pack(side="top", fill="x")

root.configure(fg_color="#bcbcbc") # Sets foreground colour but is actually background colour for main window.

window = ctk.CTkFrame(root)
# Text at the bottom of the window to let the user know if they have a file loaded or not.
status_label = Label(root, text="No file loaded", font=("Geneva", 12)) 
status_label.pack(side="bottom", pady=10) # location.

results_label = Label(root, text="", font=("Geneva", 12)) # Whatever the name of the doc will be shown, letting the user know what doc they have laoded.
results_label.pack()

# Buttons
load_button = ctk.CTkButton(
    master=root,
    text="Load Report",
    width=200,
    height=50,
    fg_color="#1d4a7d",  # OFH Blue
    hover_color="#042246",  # Slightly darker OFH Blue
    text_color="white",  # White text
    font=("Univers", 18),
    command=None 

)

quit_button = ctk.CTkButton(
    master=root,
    text="Quit",
    width=200,
    height=50,
    fg_color="#f44336",  # Red button
    hover_color="#ff0004",  # More saturated red on hover (stand out)
    text_color="white",  # White text
    font=("Univers", 18),
    command=root.destroy # makes the quit.... quit
)

# Button position
load_button.place(relx=0.5, rely=0.4, anchor="center")
quit_button.place(relx=0.5, rely=0.6, anchor="center")

print("Widgets added successfully!") # Console check.

root.mainloop()