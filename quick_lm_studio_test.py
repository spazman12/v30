#!/usr/bin/env python3
"""
Quick LM Studio connection test
Simple test to verify Cursor can connect to your LM Studio server
"""

import requests
import json
import sys

def quick_test():
    """Quick connection test"""
    print("🔍 Quick LM Studio Connection Test")
    print("=" * 40)
    
    # Common LM Studio URLs to try
    urls_to_try = [
        "http://localhost:1234",
        "http://127.0.0.1:1234",
        "http://localhost:11434",
        "http://127.0.0.1:11434"
    ]
    
    for url in urls_to_try:
        print(f"\nTesting {url}...")
        
        try:
            # Test basic connectivity
            response = requests.get(f"{url}/v1/models", timeout=5)
            
            if response.status_code == 200:
                print(f"✅ SUCCESS! LM Studio is running at {url}")
                
                # Try to get model info
                try:
                    models = response.json()
                    if 'data' in models and len(models['data']) > 0:
                        model_name = models['data'][0].get('id', 'Unknown')
                        print(f"   Model available: {model_name}")
                    else:
                        print("   No models loaded")
                except:
                    print("   Could not parse model info")
                
                # Test a simple chat completion
                try:
                    chat_payload = {
                        "model": models['data'][0]['id'] if 'data' in models and len(models['data']) > 0 else "default",
                        "messages": [{"role": "user", "content": "Hello! Test message."}],
                        "max_tokens": 10
                    }
                    
                    chat_response = requests.post(
                        f"{url}/v1/chat/completions",
                        json=chat_payload,
                        timeout=10
                    )
                    
                    if chat_response.status_code == 200:
                        print("✅ Chat completions working!")
                        result = chat_response.json()
                        if 'choices' in result and len(result['choices']) > 0:
                            reply = result['choices'][0]['message']['content']
                            print(f"   AI Response: {reply}")
                    else:
                        print(f"⚠️ Chat completions failed (status: {chat_response.status_code})")
                        
                except Exception as e:
                    print(f"⚠️ Chat test failed: {e}")
                
                print(f"\n🎉 LM Studio is working at {url}")
                return True
                
            else:
                print(f"❌ Server responded with status {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection refused - server not running")
        except requests.exceptions.Timeout:
            print("❌ Connection timeout")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n❌ Could not connect to LM Studio on any common port")
    print("\nTroubleshooting tips:")
    print("1. Make sure LM Studio is running")
    print("2. Check that the server is started (not just the UI)")
    print("3. Verify the port number in LM Studio settings")
    print("4. Try running: python quick_lm_studio_test.py http://your-custom-url:port")
    
    return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Test custom URL
        custom_url = sys.argv[1]
        print(f"Testing custom URL: {custom_url}")
        
        try:
            response = requests.get(f"{custom_url}/v1/models", timeout=5)
            if response.status_code == 200:
                print("✅ SUCCESS! Custom URL is working")
            else:
                print(f"❌ Custom URL failed with status {response.status_code}")
        except Exception as e:
            print(f"❌ Custom URL error: {e}")
    else:
        # Test common URLs
        quick_test()
