#!/usr/bin/env python3
"""
Debug script to test the application step by step
"""

import sys
import os

print("=== DEBUGGING STEAM TOOLS GENERATOR ===")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")

# Test imports one by one
print("\n=== TESTING IMPORTS ===")

try:
    import tkinter as tk
    print("✅ tkinter imported successfully")
except Exception as e:
    print(f"❌ tkinter failed: {e}")
    sys.exit(1)

try:
    import requests
    print("✅ requests imported successfully")
except Exception as e:
    print(f"❌ requests failed: {e}")

try:
    from PIL import Image
    print("✅ PIL imported successfully")
except Exception as e:
    print(f"❌ PIL failed: {e}")

# Test Steam imports exactly as the application does
print("\n=== TESTING STEAM IMPORTS ===")

try:
    from steam.client import SteamClient
    from steam.guard import generate_twofactor_code_for_time
    STEAM_AVAILABLE = True
    print("✅ ValvePython steam library loaded successfully!")
except ImportError as e:
    STEAM_AVAILABLE = False
    print(f"⚠️ Steam library not available: {e}")
    print("📦 To install: pip install steam eventemitter gevent protobuf")

print(f"STEAM_AVAILABLE: {STEAM_AVAILABLE}")

# Test importing the application
print("\n=== TESTING APPLICATION IMPORT ===")

try:
    # Change to v30 directory
    os.chdir(os.path.join(os.path.dirname(__file__), 'v30'))
    print(f"Changed to directory: {os.getcwd()}")
    
    # Import the application
    from steam_tools_generator import SteamToolsGenerator
    print("✅ SteamToolsGenerator imported successfully!")
    
    # Test creating a window
    print("\n=== TESTING GUI CREATION ===")
    root = tk.Tk()
    root.title("Debug Test")
    root.geometry("400x300")
    
    # Create the application
    app = SteamToolsGenerator(root)
    print("✅ Application created successfully!")
    
    # Test if we can show the window briefly
    root.update()
    print("✅ GUI updated successfully!")
    
    # Don't start mainloop, just test
    root.destroy()
    print("✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n=== DEBUG COMPLETE ===")



