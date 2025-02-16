# Customtkineter
import customtkinter as ctk
from customtkinter import CTkLabel, CTkScrollableFrame, CTkButton

# tkinter
import tkinter.font as tkFont
from tkinter import Tk, Label, messagebox, Scrollbar, Canvas, Frame, Toplevel

# Image prcoessing 
from PIL import Image, ImageTk 

# System utilities
import os
import sys

# handle_data script
from handle_data import load_data, analyse_data


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

def handle_load_report():
    global loaded_data
    root.withdraw() # Hide the main window when selecting file
    filename, loaded_data = load_data()
    if filename:
        status_label.configure(text=f"{os.path.basename(filename)} Loaded", fg="#0caf22")
        try:
            print("Running data analysis...") # Console check.
            analysis_summary = analyse_data(loaded_data)
            print(f"Analysis Complete: {analysis_summary}") # Console check.

            # Open a new window for displaying results
            open_analysis_window(analysis_summary)

        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            messagebox.showerror("Analysis has Failed", f"An error occurred while analysing the file: {e}")
    else:
        status_label.configure(text="No file loaded", fg="#ff0004")
    root.deiconify()  

def open_analysis_window(analysis_summary):
    # Create 'analysis_window'
    analysis_window = Toplevel(root)
    analysis_window.title("Analysis Results")  # Print Notification
    analysis_window.geometry("500x800")  # Size

    title_font = ("Geneva", 18, "bold")  # Bold font for titles
    data_font = ("Univers", 16)          # Font for regular data

    # Add a scrollable text widget
    scrollable_frame = CTkScrollableFrame(analysis_window, width=480, height=360)
    scrollable_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Order and Titles Mapping
    display_order = [
        ("Site Count", "site_counts"),
        ("Success Count", "success_count"),
        ("Success Percentage", "success_percentage"),
        ("Fail Count", "fail_count"),
        ("Fail Percentage", "fail_percentage"),
        ("Total Jobs", "total_jobs"),
        ("Driver Job Count", "driver_job_counts"),
        ("On Time Count", "on_time_counts"),
        ("Collection Window Count", "collection_window_counts")
    ]
    
    # Loop through the display order directly
    for display_title, key in display_order:
        # Fetch the value corresponding to the current key from the `analysis_summary`
        value = analysis_summary.get(key)
        
        # Check if the value is a nested dictionary
        if isinstance(value, dict):
            value = sum(value.values())  # Combine nested dictionary values into a single integer/float

        # Ensure the value is displayable (convert to string if needed)
        value_display = str(value) if value is not None else "N/A"

        # Create a label for each key-value pair
        label = CTkLabel(
            scrollable_frame,
            text=f"{display_title}: {value_display}",
            anchor="w",
            justify="left",
            font=data_font,  # Use regular font for data
        )
        label.pack(anchor="w", padx=10, pady=5)

    # Optionally add a close button to the analysis_window
    close_button = CTkButton(analysis_window, text="Close", command=analysis_window.destroy)
    close_button.pack(pady=10)



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
    command=handle_load_report

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

# Adding Logo to the top
logo_image = ctk.CTkImage(
    light_image=Image.open("image/OFH_LOGO.jpg"),
    size=(70, 70)
)
logo_label = ctk.CTkLabel(
    title_bar, 
    image=logo_image, 
    text=""
)
logo_label.pack(side="left", padx=10)  # Place logo on the left of the title bar        

title_label = ctk.CTkLabel(
    title_bar, 
    text="Report Analyser",
    fg_color=None, 
    text_color="#172264", 
    font=("geneva", 20)
)
title_label.pack(side="left", padx=10)

# Linking the drag event to the Title bar
title_bar.bind("<B1-Motion>", move_window)

root.mainloop()
print("Mainloop is running!") # Console check.