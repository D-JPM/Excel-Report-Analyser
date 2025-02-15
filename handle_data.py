# Imports
import pandas as pd
import os

from tkinter import filedialog, messagebox

def load_data(): # Left empty as files will be chosen dynamically.
    # Open file dialog for file selection (file type should only be '.xlsx).
    filename = filedialog.askopenfilename(
        title="Select an Excel file", filetypes=[("Excel files","*.xlsx")]
    )

    # Check if user has canceled the file dialog.
    if not filename: # If the user has chose to either cancel or close the dialog.
        messagebox.showwarning("No File was selected!", "Please try again.")
        return None, None # Return 'None' as no file was loaded.
    
    # File Verification.
    if not filename.endswith('.xlsx') # Make sure the file does end with .xlsx (extenstion)
        messagebox.showerror("Invalid File", "The selected file is not an Excel (.xlsx) file!")
        return None, None # Exit if the filetype is invalid.
    # If the filetype is valid....
    try:
        data = pd.read_excel(filename) # Read the file.
        print(f"shape of data: {data.shape}") # Debuggin in console. Want to see dimensions in the console.
        return filename, data # Retunr the filename and the data.
    except Exception as e: # Handle any errors during the file loading.
        messagebox.showerror("Error reading file", f"an error has occured: {e}")
        return None, None
    
def analyse_data(data):
    if data is None or data.empty: # Check if the dataset is empty or not.
        return None # Exit the function if the ds is empty.
    print("Running data analysis....") # Console check.

    site_name_counts = data["SITE NAME"].value_counts()
    print(f"Site Name Counts:\n{site_name_counts}") # Console check.

    