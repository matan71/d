import os
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog

# Create a root window (it will not be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a dialog to select a folder
folder_selected = filedialog.askdirectory()

if folder_selected:
    print(f"Contents of the folder '{folder_selected}':\n")
    
    # Walk through the folder and list all files and subfolders
    for root, dirs, files in os.walk(folder_selected):
        print(f"Folder: {root}")
        
        for name in dirs:
            
        
        for name in files:
            
r=requests.get("https://www.virustotal.com/gui/home/upload" % folder_selected, headers=("") )   
print("No folder was selected.")