#!/usr/bin/env python3
"""
Test script to check what's working with imports
"""

print("Testing basic imports...")

try:
    import tkinter as tk
    print("✅ tkinter imported successfully")
except ImportError as e:
    print(f"❌ tkinter import failed: {e}")

try:
    import requests
    print("✅ requests imported successfully")
except ImportError as e:
    print(f"❌ requests import failed: {e}")

try:
    from PIL import Image
    print("✅ PIL imported successfully")
except ImportError as e:
    print(f"❌ PIL import failed: {e}")

try:
    import steam
    print("✅ steam imported successfully")
except ImportError as e:
    print(f"❌ steam import failed: {e}")

try:
    from steam.client import SteamClient
    print("✅ SteamClient imported successfully")
except ImportError as e:
    print(f"❌ SteamClient import failed: {e}")

try:
    from steam.guard import generate_twofactor_code_for_time
    print("✅ generate_twofactor_code_for_time imported successfully")
except ImportError as e:
    print(f"❌ generate_twofactor_code_for_time import failed: {e}")

print("Import test complete!")
