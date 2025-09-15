#!/usr/bin/env python3
"""
Minimal test to check if the application can import
"""

import sys
import os

print("=== MINIMAL APPLICATION TEST ===")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")

# Test basic imports
try:
    import tkinter as tk
    print("✅ tkinter available")
except Exception as e:
    print(f"❌ tkinter failed: {e}")
    sys.exit(1)

try:
    import requests
    print("✅ requests available")
except Exception as e:
    print(f"❌ requests failed: {e}")

try:
    from PIL import Image
    print("✅ PIL available")
except Exception as e:
    print(f"❌ PIL failed: {e}")

# Test Steam imports
try:
    import steam
    print("✅ steam available")
    try:
        from steam.client import SteamClient
        print("✅ SteamClient available")
    except Exception as e:
        print(f"❌ SteamClient failed: {e}")
except Exception as e:
    print(f"❌ steam failed: {e}")

print("\n=== ATTEMPTING TO IMPORT APPLICATION ===")

# Change to v30 directory
os.chdir(os.path.join(os.path.dirname(__file__), 'v30'))
print(f"Changed to directory: {os.getcwd()}")

try:
    # Try to import just the class
    from steam_tools_generator import SteamToolsGenerator
    print("✅ SteamToolsGenerator class imported successfully!")
    
    # Try to create a simple tkinter window
    root = tk.Tk()
    root.title("Test Window")
    root.geometry("400x300")
    
    # Try to create the application
    app = SteamToolsGenerator(root)
    print("✅ Application created successfully!")
    
    # Don't start mainloop, just test creation
    root.destroy()
    print("✅ Application test completed successfully!")
    
except Exception as e:
    print(f"❌ Application import/creation failed: {e}")
    import traceback
    traceback.print_exc()

print("\n=== TEST COMPLETE ===")
