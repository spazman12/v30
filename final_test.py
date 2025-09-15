#!/usr/bin/env python3
"""
Final test to verify the application works
"""

import sys
import os

print("=== FINAL APPLICATION TEST ===")

# Change to v30 directory
os.chdir(os.path.join(os.path.dirname(__file__), 'v30'))
print(f"Working directory: {os.getcwd()}")

try:
    print("Importing application...")
    from steam_tools_generator import main
    print("✅ Application imported successfully!")
    
    print("Starting application...")
    main()
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("Test complete.")



