# Imports
import pandas as pd
from tkinter import filedialog, messagebox
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
    if not filename.endswith('.xlsx'): # Make sure the file does end with .xlsx (extenstion)
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

    # Analysing Job success & Failures
    successful_jobs = data["SUCCESSFUL JOB"].value_counts()
    total_jobs = len(data)
    success_count = successful_jobs.get("YES", 0)
    fail_count = successful_jobs.get("NO", 0)
    success_percentage = (success_count / total_jobs) * 100 if total_jobs > 0 else 0
    fail_percentage = (fail_count / total_jobs) * 100 if total_jobs > 0 else 0

     # Driver job completion count
    driver_job_counts = data["DRIVER NAME"].value_counts()

    # On-Time analysis 
    on_time_counts = data[data["ON TIME"] == "YES"]["DRIVER NAME"].value_counts() 

    # Collection Window Count
    collection_window_counts = data["COLLECTION WINDOW"].value_counts()

    # Result Dict
    summary = {
        "site_counts": site_name_counts.to_dict(),
        "success_count": success_count,
        "fail_count": fail_count,
        "success_percentage": round(success_percentage, 2),
        "fail_percentage": round(fail_percentage, 2),
        "total_jobs": total_jobs,
        "driver_job_counts": driver_job_counts.to_dict(), 
        "on_time_counts": on_time_counts.to_dict(),
        "collection_window_counts": collection_window_counts.to_dict(),
    }

    return summary