#!/usr/bin/env python3
"""
Test LM Studio integration with Steam Tools Generator
Tests AI-powered features and content generation
"""

import requests
import json
import time
import sys
import os
from typing import Dict, Any, Optional, List

class LMStudioSteamIntegrationTester:
    def __init__(self, lm_studio_url: str = "http://localhost:1234"):
        self.lm_studio_url = lm_studio_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'SteamTools-LMStudio-Integration/1.0'
        })
        self.model_id = None
    
    def setup_model(self) -> bool:
        """Setup and verify model is available"""
        try:
            print("🔍 Setting up LM Studio model...")
            
            # Get available models
            response = self.session.get(f"{self.lm_studio_url}/v1/models", timeout=10)
            if response.status_code != 200:
                print("❌ Failed to get models list")
                return False
            
            models_data = response.json()
            if 'data' not in models_data or len(models_data['data']) == 0:
                print("❌ No models available")
                return False
            
            # Use the first available model
            self.model_id = models_data['data'][0]['id']
            print(f"✅ Using model: {self.model_id}")
            return True
            
        except Exception as e:
            print(f"❌ Model setup failed: {e}")
            return False
    
    def test_game_description_generation(self) -> bool:
        """Test AI generation of game descriptions"""
        try:
            print("\n🎮 Testing game description generation...")
            
            prompt = """Generate a brief, engaging description for a Steam game. 
            Include the game's genre, key features, and what makes it unique.
            Keep it under 200 words and make it sound professional.
            
            Game: Cyberpunk 2077
            Genre: Action RPG
            """
            
            payload = {
                "model": self.model_id,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 300,
                "temperature": 0.7
            }
            
            response = self.session.post(
                f"{self.lm_studio_url}/v1/chat/completions",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'choices' in result and len(result['choices']) > 0:
                    description = result['choices'][0]['message']['content']
                    print("✅ Game description generated successfully")
                    print(f"   Description: {description[:200]}...")
                    return True
                else:
                    print("❌ No response content generated")
                    return False
            else:
                print(f"❌ Generation failed with status {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Game description generation error: {e}")
            return False
    
    def test_lua_script_optimization(self) -> bool:
        """Test AI optimization of Lua scripts"""
        try:
            print("\n🔧 Testing Lua script optimization...")
            
            sample_lua = """
-- Basic Steam Tools Lua script
addappid(123456, 1, "key123")
setManifestid(123456, "manifest456", 1000000)
downloadapp(123456)
"""
            
            prompt = f"""Optimize this Steam Tools Lua script for better performance and add helpful comments.
            Make sure it follows best practices for Steam Tools.
            
            Script to optimize:
            ```lua
            {sample_lua}
            ```
            
            Return only the optimized Lua code with comments.
            """
            
            payload = {
                "model": self.model_id,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 500,
                "temperature": 0.3
            }
            
            response = self.session.post(
                f"{self.lm_studio_url}/v1/chat/completions",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'choices' in result and len(result['choices']) > 0:
                    optimized_script = result['choices'][0]['message']['content']
                    print("✅ Lua script optimization successful")
                    print(f"   Optimized script preview: {optimized_script[:300]}...")
                    return True
                else:
                    print("❌ No optimized script generated")
                    return False
            else:
                print(f"❌ Optimization failed with status {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Lua script optimization error: {e}")
            return False
    
    def test_error_diagnosis(self) -> bool:
        """Test AI-powered error diagnosis"""
        try:
            print("\n🔍 Testing error diagnosis...")
            
            error_scenario = """
            Steam Tools Error: "Failed to decrypt depot manifest"
            App ID: 123456
            Depot ID: 123456
            Manifest ID: 7890123456789012345
            Decryption Key: aabbccddeeff...
            """
            
            prompt = f"""Diagnose this Steam Tools error and provide a solution.
            Consider common causes like incorrect decryption keys, invalid manifest IDs, or network issues.
            
            Error details:
            {error_scenario}
            
            Provide:
            1. Likely cause of the error
            2. Step-by-step solution
            3. Prevention tips
            """
            
            payload = {
                "model": self.model_id,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 400,
                "temperature": 0.5
            }
            
            response = self.session.post(
                f"{self.lm_studio_url}/v1/chat/completions",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'choices' in result and len(result['choices']) > 0:
                    diagnosis = result['choices'][0]['message']['content']
                    print("✅ Error diagnosis successful")
                    print(f"   Diagnosis: {diagnosis[:300]}...")
                    return True
                else:
                    print("❌ No diagnosis generated")
                    return False
            else:
                print(f"❌ Error diagnosis failed with status {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error diagnosis error: {e}")
            return False
    
    def test_batch_processing(self) -> bool:
        """Test batch processing of multiple requests"""
        try:
            print("\n📦 Testing batch processing...")
            
            # Test multiple quick requests
            test_prompts = [
                "What is Steam Tools?",
                "How do I generate a decryption key?",
                "What is a manifest ID?",
                "How do I use Steam Tools Lua scripts?"
            ]
            
            success_count = 0
            for i, prompt in enumerate(test_prompts, 1):
                print(f"   Processing request {i}/{len(test_prompts)}...")
                
                payload = {
                    "model": self.model_id,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "max_tokens": 100,
                    "temperature": 0.7
                }
                
                response = self.session.post(
                    f"{self.lm_studio_url}/v1/chat/completions",
                    json=payload,
                    timeout=15
                )
                
                if response.status_code == 200:
                    success_count += 1
                else:
                    print(f"   ❌ Request {i} failed")
            
            success_rate = (success_count / len(test_prompts)) * 100
            print(f"✅ Batch processing: {success_count}/{len(test_prompts)} requests successful ({success_rate:.1f}%)")
            
            return success_rate >= 75
            
        except Exception as e:
            print(f"❌ Batch processing error: {e}")
            return False
    
    def test_performance_metrics(self) -> Dict[str, float]:
        """Test performance metrics"""
        try:
            print("\n⚡ Testing performance metrics...")
            
            metrics = {}
            
            # Test response time
            start_time = time.time()
            
            payload = {
                "model": self.model_id,
                "messages": [
                    {
                        "role": "user",
                        "content": "Generate a short Steam game description for testing performance."
                    }
                ],
                "max_tokens": 50,
                "temperature": 0.7
            }
            
            response = self.session.post(
                f"{self.lm_studio_url}/v1/chat/completions",
                json=payload,
                timeout=30
            )
            
            end_time = time.time()
            response_time = end_time - start_time
            metrics['response_time'] = response_time
            
            if response.status_code == 200:
                result = response.json()
                if 'usage' in result:
                    metrics['tokens_generated'] = result['usage'].get('completion_tokens', 0)
                    metrics['total_tokens'] = result['usage'].get('total_tokens', 0)
                
                tokens_per_second = metrics.get('tokens_generated', 0) / max(response_time, 0.001)
                metrics['tokens_per_second'] = tokens_per_second
                
                print(f"✅ Response time: {response_time:.2f}s")
                print(f"✅ Tokens generated: {metrics.get('tokens_generated', 'N/A')}")
                print(f"✅ Tokens per second: {tokens_per_second:.2f}")
                
            else:
                print(f"❌ Performance test failed with status {response.status_code}")
            
            return metrics
            
        except Exception as e:
            print(f"❌ Performance test error: {e}")
            return {}
    
    def run_integration_tests(self) -> Dict[str, bool]:
        """Run all integration tests"""
        print("=" * 70)
        print("🚀 LM STUDIO STEAM TOOLS INTEGRATION TEST")
        print("=" * 70)
        print(f"Testing integration with: {self.lm_studio_url}")
        print()
        
        results = {}
        
        # Setup
        if not self.setup_model():
            print("❌ Model setup failed. Cannot continue with tests.")
            return results
        
        # Run tests
        results['game_description'] = self.test_game_description_generation()
        results['lua_optimization'] = self.test_lua_script_optimization()
        results['error_diagnosis'] = self.test_error_diagnosis()
        results['batch_processing'] = self.test_batch_processing()
        
        # Performance test
        performance_metrics = self.test_performance_metrics()
        results['performance'] = len(performance_metrics) > 0
        
        # Summary
        print("\n" + "=" * 70)
        print("📊 INTEGRATION TEST RESULTS")
        print("=" * 70)
        
        for test_name, passed in results.items():
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"{test_name.replace('_', ' ').title()}: {status}")
        
        if performance_metrics:
            print(f"\nPerformance Metrics:")
            for metric, value in performance_metrics.items():
                print(f"  {metric.replace('_', ' ').title()}: {value:.2f}")
        
        total_tests = len(results)
        passed_tests = sum(results.values())
        success_rate = (passed_tests / total_tests) * 100
        
        print(f"\nOverall Success Rate: {passed_tests}/{total_tests} ({success_rate:.1f}%)")
        
        if success_rate >= 80:
            print("🎉 LM Studio integration is working excellently!")
        elif success_rate >= 60:
            print("⚠️ LM Studio integration has some issues but is functional")
        else:
            print("❌ LM Studio integration has major issues")
        
        return results

def main():
    """Main test function"""
    print("LM Studio Steam Tools Integration Tester")
    print("=" * 50)
    
    # Check if custom URL provided
    if len(sys.argv) > 1:
        custom_url = sys.argv[1]
        print(f"Using custom LM Studio URL: {custom_url}")
        tester = LMStudioSteamIntegrationTester(custom_url)
    else:
        tester = LMStudioSteamIntegrationTester()
    
    # Run integration tests
    results = tester.run_integration_tests()
    
    # Exit with appropriate code
    if all(results.values()):
        sys.exit(0)  # All tests passed
    else:
        sys.exit(1)  # Some tests failed

if __name__ == "__main__":
    main()
