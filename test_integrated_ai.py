#!/usr/bin/env python3
"""
Test the integrated LM Studio functionality in Steam Tools Generator
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

# Add v30 directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v30'))

def test_lm_studio_integration():
    """Test LM Studio integration"""
    print("🧪 Testing LM Studio Integration...")
    
    try:
        # Import the integration
        from lm_studio_integration import LMStudioIntegration
        print("✅ LM Studio integration imported successfully")
        
        # Test connection
        lm_studio = LMStudioIntegration()
        if lm_studio.is_available():
            print("✅ LM Studio is available and connected")
            print(f"   Model: {lm_studio.model_id}")
            
            # Test basic generation
            test_prompt = "Hello! This is a test of the LM Studio integration."
            response = lm_studio.generate_text(test_prompt, max_tokens=20)
            
            if response:
                print(f"✅ Text generation working: {response[:50]}...")
            else:
                print("❌ Text generation failed")
                return False
                
        else:
            print("❌ LM Studio is not available")
            return False
            
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False
    
    return True

def test_steam_tools_generator():
    """Test Steam Tools Generator with AI integration"""
    print("\n🧪 Testing Steam Tools Generator with AI...")
    
    try:
        # Import the main class
        from steam_tools_generator import SteamToolsGenerator
        print("✅ Steam Tools Generator imported successfully")
        
        # Create a test window
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        # Create the generator
        generator = SteamToolsGenerator(root)
        print("✅ Steam Tools Generator created successfully")
        
        # Check if LM Studio is integrated
        if hasattr(generator, 'lm_studio') and generator.lm_studio:
            print("✅ LM Studio integration found in generator")
            
            if generator.lm_studio.is_available():
                print("✅ LM Studio is available in generator")
                print(f"   Model: {generator.lm_studio.model_id}")
            else:
                print("⚠️ LM Studio is not available in generator")
        else:
            print("❌ LM Studio integration not found in generator")
            return False
        
        # Test AI features availability
        if hasattr(generator, 'show_ai_features'):
            print("✅ AI features method found")
        else:
            print("❌ AI features method not found")
            return False
        
        # Clean up
        root.destroy()
        
    except Exception as e:
        print(f"❌ Steam Tools Generator test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("🚀 LM STUDIO INTEGRATION TEST SUITE")
    print("=" * 60)
    
    tests = [
        ("LM Studio Integration", test_lm_studio_integration),
        ("Steam Tools Generator with AI", test_steam_tools_generator)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 40)
        try:
            result = test_func()
            results.append((test_name, result))
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{status} {test_name}")
        except Exception as e:
            print(f"❌ FAIL {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! LM Studio integration is working perfectly!")
        return True
    else:
        print("⚠️ Some tests failed. Check the output above for details.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
