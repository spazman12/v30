#!/usr/bin/env python3
"""
Simple test to see if we can at least open a basic GUI
"""

import tkinter as tk
from tkinter import ttk

def test_basic_gui():
    print("Creating basic GUI test...")
    
    root = tk.Tk()
    root.title("Test Window")
    root.geometry("400x300")
    
    # Add a simple label
    label = tk.Label(root, text="If you can see this, GUI is working!", font=("Arial", 16))
    label.pack(pady=50)
    
    # Add a button
    button = tk.Button(root, text="Test Button", command=lambda: print("Button clicked!"))
    button.pack(pady=20)
    
    print("GUI created successfully!")
    print("Starting mainloop...")
    
    # Start the GUI
    root.mainloop()
    
    print("GUI closed.")

if __name__ == "__main__":
    try:
        test_basic_gui()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()



