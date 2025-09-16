#!/usr/bin/env python3
"""
Test script to check connection to LM Studio server
Tests various LM Studio API endpoints and configurations
"""

import requests
import json
import time
import sys
from typing import Dict, Any, Optional

class LMStudioConnectionTester:
    def __init__(self, base_url: str = "http://localhost:1234"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'LMStudio-Connection-Tester/1.0'
        })
    
    def test_server_health(self) -> bool:
        """Test if LM Studio server is running and accessible"""
        try:
            print(f"🔍 Testing LM Studio server health at {self.base_url}...")
            
            # Test basic connectivity
            response = self.session.get(f"{self.base_url}/v1/models", timeout=5)
            
            if response.status_code == 200:
                print("✅ LM Studio server is running and accessible")
                return True
            else:
                print(f"❌ Server responded with status {response.status_code}")
                return False
                
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to LM Studio server at {self.base_url}")
            print("   Make sure LM Studio is running and the server is started")
            return False
        except requests.exceptions.Timeout:
            print("❌ Connection timeout - server may be overloaded")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False
    
    def test_models_endpoint(self) -> Optional[Dict[str, Any]]:
        """Test the /v1/models endpoint"""
        try:
            print("\n🔍 Testing /v1/models endpoint...")
            response = self.session.get(f"{self.base_url}/v1/models", timeout=10)
            
            if response.status_code == 200:
                models_data = response.json()
                print("✅ Models endpoint accessible")
                print(f"   Response: {json.dumps(models_data, indent=2)}")
                return models_data
            else:
                print(f"❌ Models endpoint failed with status {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Models endpoint error: {e}")
            return None
    
    def test_chat_completions(self, model_id: str = None) -> bool:
        """Test the /v1/chat/completions endpoint"""
        try:
            print(f"\n🔍 Testing /v1/chat/completions endpoint...")
            
            # If no model specified, try to get the first available model
            if not model_id:
                models_data = self.test_models_endpoint()
                if models_data and 'data' in models_data and len(models_data['data']) > 0:
                    model_id = models_data['data'][0]['id']
                    print(f"   Using model: {model_id}")
                else:
                    print("❌ No models available for testing")
                    return False
            
            # Test chat completion
            payload = {
                "model": model_id,
                "messages": [
                    {
                        "role": "user",
                        "content": "Hello! This is a connection test. Please respond with 'Connection successful!'"
                    }
                ],
                "max_tokens": 50,
                "temperature": 0.7
            }
            
            response = self.session.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Chat completions endpoint working")
                if 'choices' in result and len(result['choices']) > 0:
                    content = result['choices'][0]['message']['content']
                    print(f"   Response: {content}")
                return True
            else:
                print(f"❌ Chat completions failed with status {response.status_code}")
                print(f"   Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Chat completions error: {e}")
            return False
    
    def test_completions_endpoint(self, model_id: str = None) -> bool:
        """Test the /v1/completions endpoint"""
        try:
            print(f"\n🔍 Testing /v1/completions endpoint...")
            
            if not model_id:
                models_data = self.test_models_endpoint()
                if models_data and 'data' in models_data and len(models_data['data']) > 0:
                    model_id = models_data['data'][0]['id']
                    print(f"   Using model: {model_id}")
                else:
                    print("❌ No models available for testing")
                    return False
            
            payload = {
                "model": model_id,
                "prompt": "Complete this sentence: The quick brown fox",
                "max_tokens": 20,
                "temperature": 0.7
            }
            
            response = self.session.post(
                f"{self.base_url}/v1/completions",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Completions endpoint working")
                if 'choices' in result and len(result['choices']) > 0:
                    text = result['choices'][0]['text']
                    print(f"   Response: {text}")
                return True
            else:
                print(f"❌ Completions failed with status {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Completions error: {e}")
            return False
    
    def test_server_info(self) -> Optional[Dict[str, Any]]:
        """Test server information endpoints"""
        try:
            print(f"\n🔍 Testing server information...")
            
            # Try to get server info (this endpoint may not exist in all LM Studio versions)
            try:
                response = self.session.get(f"{self.base_url}/v1/server/info", timeout=5)
                if response.status_code == 200:
                    info = response.json()
                    print("✅ Server info available")
                    print(f"   Info: {json.dumps(info, indent=2)}")
                    return info
            except:
                pass
            
            # Test health endpoint
            try:
                response = self.session.get(f"{self.base_url}/health", timeout=5)
                if response.status_code == 200:
                    print("✅ Health endpoint available")
                    print(f"   Health: {response.text}")
            except:
                pass
            
            return None
            
        except Exception as e:
            print(f"❌ Server info error: {e}")
            return None
    
    def run_full_test(self) -> Dict[str, bool]:
        """Run all tests and return results"""
        print("=" * 60)
        print("🚀 LM STUDIO CONNECTION TEST")
        print("=" * 60)
        print(f"Testing connection to: {self.base_url}")
        print()
        
        results = {}
        
        # Test 1: Basic connectivity
        results['server_health'] = self.test_server_health()
        
        if not results['server_health']:
            print("\n❌ Server not accessible. Stopping tests.")
            return results
        
        # Test 2: Models endpoint
        models_data = self.test_models_endpoint()
        results['models_endpoint'] = models_data is not None
        
        # Test 3: Chat completions
        model_id = None
        if models_data and 'data' in models_data and len(models_data['data']) > 0:
            model_id = models_data['data'][0]['id']
        
        results['chat_completions'] = self.test_chat_completions(model_id)
        
        # Test 4: Completions endpoint
        results['completions'] = self.test_completions_endpoint(model_id)
        
        # Test 5: Server info
        server_info = self.test_server_info()
        results['server_info'] = server_info is not None
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 60)
        
        for test_name, passed in results.items():
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"{test_name.replace('_', ' ').title()}: {status}")
        
        total_tests = len(results)
        passed_tests = sum(results.values())
        success_rate = (passed_tests / total_tests) * 100
        
        print(f"\nOverall Success Rate: {passed_tests}/{total_tests} ({success_rate:.1f}%)")
        
        if success_rate >= 80:
            print("🎉 LM Studio connection is working well!")
        elif success_rate >= 50:
            print("⚠️ LM Studio connection has some issues")
        else:
            print("❌ LM Studio connection has major issues")
        
        return results

def test_different_ports():
    """Test common LM Studio ports"""
    common_ports = [1234, 11434, 8080, 8000, 3000]
    
    print("\n🔍 Testing common LM Studio ports...")
    
    for port in common_ports:
        url = f"http://localhost:{port}"
        print(f"\nTesting {url}...")
        
        tester = LMStudioConnectionTester(url)
        if tester.test_server_health():
            print(f"✅ Found LM Studio server at {url}")
            return url
    
    print("❌ No LM Studio server found on common ports")
    return None

def main():
    """Main test function"""
    print("LM Studio Connection Tester")
    print("=" * 40)
    
    # Check if custom URL provided
    if len(sys.argv) > 1:
        custom_url = sys.argv[1]
        print(f"Using custom URL: {custom_url}")
        tester = LMStudioConnectionTester(custom_url)
    else:
        # Try default port first
        tester = LMStudioConnectionTester()
        if not tester.test_server_health():
            # If default fails, try other common ports
            found_url = test_different_ports()
            if found_url:
                tester = LMStudioConnectionTester(found_url)
            else:
                print("\n❌ Could not find LM Studio server")
                print("Make sure LM Studio is running and the server is started")
                return
    
    # Run full test suite
    results = tester.run_full_test()
    
    # Exit with appropriate code
    if all(results.values()):
        sys.exit(0)  # All tests passed
    else:
        sys.exit(1)  # Some tests failed

if __name__ == "__main__":
    main()
