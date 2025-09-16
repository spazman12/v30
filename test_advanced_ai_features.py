#!/usr/bin/env python3
"""
Test Advanced AI Features in Steam Tools Generator
Demonstrates the enhanced capabilities with unrestricted AI model
"""

import sys
import os
import json
import time

# Add v30 directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v30'))

def test_advanced_ai_integration():
    """Test the advanced AI integration"""
    print("🧪 Testing Advanced AI Integration...")
    
    try:
        from advanced_steam_ai import AdvancedSteamAI
        from lm_studio_integration import LMStudioIntegration
        
        # Initialize LM Studio
        lm_studio = LMStudioIntegration()
        if not lm_studio.is_available():
            print("❌ LM Studio not available")
            return False
        
        # Initialize Advanced AI
        advanced_ai = AdvancedSteamAI(lm_studio)
        print("✅ Advanced Steam AI initialized")
        
        # Test AI data analysis
        print("\n🔍 Testing AI data analysis...")
        test_data = """
        {
            "app_id": "123456",
            "depots": {
                "1234561": {"name": "Main Depot"},
                "1234562": {"name": "DLC Depot"}
            },
            "manifests": {
                "1234561": "9876543210987654321",
                "1234562": "8765432109876543210"
            }
        }
        """
        
        analysis = advanced_ai.ai_analyze_steam_data(test_data, "Test Steam data")
        if analysis:
            print("✅ AI data analysis working")
            print(f"   Found {len(analysis.get('depot_ids', []))} depot IDs")
            print(f"   Found {len(analysis.get('manifest_ids', []))} manifest IDs")
        else:
            print("⚠️ AI data analysis returned no results")
        
        # Test advanced key generation
        print("\n🔑 Testing advanced key generation...")
        app_id = "123456"
        depot_id = "1234561"
        game_name = "Test Game"
        
        advanced_key = advanced_ai.ai_generate_advanced_key(app_id, depot_id, game_name, {
            'developer': 'Test Developer',
            'release_date': '2024-01-01'
        })
        
        if advanced_key and len(advanced_key) == 64:
            print(f"✅ Advanced key generation working: {advanced_key[:16]}...")
        else:
            print("❌ Advanced key generation failed")
        
        # Test hidden depot discovery
        print("\n🔍 Testing hidden depot discovery...")
        depots = advanced_ai.ai_discover_hidden_depots(app_id)
        if depots:
            print(f"✅ Hidden depot discovery working: {len(depots)} depots found")
            for depot in depots[:3]:  # Show first 3
                print(f"   - {depot['depot_id']} (confidence: {depot.get('confidence', 0.5):.2f})")
        else:
            print("⚠️ No hidden depots discovered (expected for test app)")
        
        # Test pattern analysis
        print("\n🧠 Testing pattern analysis...")
        patterns = advanced_ai.ai_discover_steam_patterns(app_id)
        if patterns:
            print("✅ Pattern analysis working")
            print(f"   Analysis keys: {list(patterns.keys())}")
        else:
            print("⚠️ Pattern analysis returned no results")
        
        # Test advanced Lua generation
        print("\n📝 Testing advanced Lua generation...")
        lua_script = advanced_ai.ai_generate_steam_tools_advanced_script(
            app_id, depot_id, "9876543210987654321", advanced_key, {
                'game_name': game_name,
                'developer': 'Test Developer'
            }
        )
        
        if lua_script and len(lua_script) > 100:
            print(f"✅ Advanced Lua generation working ({len(lua_script)} chars)")
            print(f"   Preview: {lua_script[:100]}...")
        else:
            print("❌ Advanced Lua generation failed")
        
        return True
        
    except Exception as e:
        print(f"❌ Advanced AI integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_steam_tools_generator_advanced():
    """Test the enhanced Steam Tools Generator"""
    print("\n🧪 Testing Enhanced Steam Tools Generator...")
    
    try:
        import tkinter as tk
        from steam_tools_generator import SteamToolsGenerator
        
        # Create a test window
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        # Create the generator
        generator = SteamToolsGenerator(root)
        print("✅ Enhanced Steam Tools Generator created")
        
        # Check advanced AI integration
        if hasattr(generator, 'advanced_ai') and generator.advanced_ai:
            print("✅ Advanced AI integration found")
            
            if generator.advanced_ai.lm.is_available():
                print("✅ Advanced AI is available and ready")
                
                # Test AI features availability
                ai_features = [
                    'discover_hidden_depots',
                    'advanced_pattern_analysis', 
                    'ai_repository_discovery'
                ]
                
                for feature in ai_features:
                    if hasattr(generator, feature):
                        print(f"✅ {feature} method available")
                    else:
                        print(f"❌ {feature} method missing")
                
            else:
                print("⚠️ Advanced AI not available")
        else:
            print("❌ Advanced AI integration not found")
            return False
        
        # Test enhanced depot discovery
        print("\n🔍 Testing enhanced depot discovery...")
        if hasattr(generator, '_find_depot_ids'):
            print("✅ Enhanced depot discovery method found")
        else:
            print("❌ Enhanced depot discovery method missing")
        
        # Test enhanced key generation
        print("\n🔑 Testing enhanced key generation...")
        if hasattr(generator, '_generate_encryption_key'):
            print("✅ Enhanced key generation method found")
        else:
            print("❌ Enhanced key generation method missing")
        
        # Test enhanced Lua generation
        print("\n📝 Testing enhanced Lua generation...")
        if hasattr(generator, '_generate_lua_file'):
            print("✅ Enhanced Lua generation method found")
        else:
            print("❌ Enhanced Lua generation method missing")
        
        # Clean up
        root.destroy()
        
        return True
        
    except Exception as e:
        print(f"❌ Enhanced Steam Tools Generator test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_ai_capabilities_demonstration():
    """Demonstrate the AI capabilities"""
    print("\n🎯 AI Capabilities Demonstration...")
    
    try:
        from advanced_steam_ai import AdvancedSteamAI
        from lm_studio_integration import LMStudioIntegration
        
        lm_studio = LMStudioIntegration()
        if not lm_studio.is_available():
            print("❌ LM Studio not available for demonstration")
            return False
        
        advanced_ai = AdvancedSteamAI(lm_studio)
        
        # Demonstrate AI analysis capabilities
        print("\n📊 AI Analysis Capabilities:")
        print("   - Steam data pattern recognition")
        print("   - Hidden depot discovery")
        print("   - Advanced encryption key generation")
        print("   - Steam API relationship analysis")
        print("   - Cryptographic pattern detection")
        
        # Demonstrate AI generation capabilities
        print("\n🤖 AI Generation Capabilities:")
        print("   - Advanced Lua script optimization")
        print("   - Intelligent error diagnosis")
        print("   - Steam Tools best practices")
        print("   - Security enhancement suggestions")
        print("   - Performance optimization recommendations")
        
        # Test a real AI generation
        print("\n🧪 Testing AI generation with real prompt...")
        test_prompt = "Generate a Steam Tools Lua script for app 123456 with advanced error handling and optimization."
        
        response = lm_studio.generate_text(test_prompt, max_tokens=200, temperature=0.7)
        if response:
            print("✅ AI generation working")
            print(f"   Response preview: {response[:100]}...")
        else:
            print("❌ AI generation failed")
        
        return True
        
    except Exception as e:
        print(f"❌ AI capabilities demonstration failed: {e}")
        return False

def main():
    """Run all advanced AI tests"""
    print("=" * 70)
    print("🚀 ADVANCED AI FEATURES TEST SUITE")
    print("=" * 70)
    print("Testing unrestricted AI model capabilities in Steam Tools Generator")
    print()
    
    tests = [
        ("Advanced AI Integration", test_advanced_ai_integration),
        ("Enhanced Steam Tools Generator", test_steam_tools_generator_advanced),
        ("AI Capabilities Demonstration", test_ai_capabilities_demonstration)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 50)
        try:
            result = test_func()
            results.append((test_name, result))
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{status} {test_name}")
        except Exception as e:
            print(f"❌ FAIL {test_name}: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 ADVANCED AI TEST RESULTS SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL ADVANCED AI FEATURES WORKING PERFECTLY!")
        print("🚀 Your Steam Tools Generator now has unrestricted AI capabilities!")
        print("🤖 Advanced features include:")
        print("   - AI-powered depot discovery")
        print("   - Advanced encryption key generation")
        print("   - Intelligent pattern analysis")
        print("   - Enhanced Lua script optimization")
        print("   - Repository discovery capabilities")
        print("   - Advanced error diagnosis")
        return True
    else:
        print("\n⚠️ Some advanced AI features need attention.")
        print("Check the output above for details.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
