#!/usr/bin/env python3
"""
Simple launcher to test the Steam Tools Generator application
"""

import sys
import os

# Add the v30 directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v30'))

try:
    print("Starting Steam Tools Generator...")
    from steam_tools_generator import main
    print("Application imported successfully!")
    print("Launching GUI...")
    main()
except Exception as e:
    print(f"Error launching application: {e}")
    import traceback
    traceback.print_exc()
