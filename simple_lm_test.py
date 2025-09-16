#!/usr/bin/env python3
"""
Simple LM Studio test
"""

import requests
import json

def test_lm_studio():
    try:
        print("Testing LM Studio connection...")
        
        # Test models endpoint
        response = requests.get("http://localhost:1234/v1/models", timeout=5)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Connection successful!")
            print(f"Models available: {len(data.get('data', []))}")
            
            if data.get('data'):
                model = data['data'][0]
                print(f"Model ID: {model.get('id', 'Unknown')}")
                print(f"Model Object: {model.get('object', 'Unknown')}")
            
            return True
        else:
            print(f"❌ Connection failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_lm_studio()
