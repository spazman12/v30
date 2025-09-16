#!/usr/bin/env python3
"""
Test LM Studio chat completions
"""

import requests
import json

def test_chat_completion():
    try:
        print("Testing LM Studio chat completion...")
        
        # Get available models first
        models_response = requests.get("http://localhost:1234/v1/models", timeout=5)
        if models_response.status_code != 200:
            print("❌ Cannot get models")
            return False
        
        models_data = models_response.json()
        if not models_data.get('data'):
            print("❌ No models available")
            return False
        
        model_id = models_data['data'][0]['id']
        print(f"Using model: {model_id}")
        
        # Test chat completion
        payload = {
            "model": model_id,
            "messages": [
                {
                    "role": "user",
                    "content": "Hello! Please respond with 'Connection test successful!'"
                }
            ],
            "max_tokens": 20,
            "temperature": 0.7
        }
        
        print("Sending chat request...")
        response = requests.post(
            "http://localhost:1234/v1/chat/completions",
            json=payload,
            timeout=30
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Chat completion successful!")
            
            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                print(f"AI Response: {content}")
            
            if 'usage' in result:
                usage = result['usage']
                print(f"Tokens used: {usage.get('total_tokens', 'Unknown')}")
            
            return True
        else:
            print(f"❌ Chat completion failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_chat_completion()
