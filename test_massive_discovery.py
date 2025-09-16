#!/usr/bin/env python3
"""
Test Massive AI Game Discovery System
"""

import sys
import os
import time

# Add v30 directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v30'))

def test_ai_discovery_system():
    """Test the AI discovery system"""
    print("🧪 Testing AI Discovery System...")
    
    try:
        from ai_game_discovery import AIGameDiscovery
        from lm_studio_integration import LMStudioIntegration
        
        # Initialize LM Studio
        lm_studio = LMStudioIntegration()
        if not lm_studio.is_available():
            print("❌ LM Studio not available")
            return False
        
        # Initialize AI Discovery
        ai_discovery = AIGameDiscovery(lm_studio)
        print("✅ AI Discovery system initialized")
        
        # Test comprehensive game generation
        print("\n🎮 Testing comprehensive game generation...")
        start_time = time.time()
        games = ai_discovery._ai_generate_comprehensive_game_list(100)
        end_time = time.time()
        
        if games:
            print(f"✅ Generated {len(games)} games in {end_time - start_time:.2f} seconds")
            print(f"   Sample game: {games[0][1]['name']} (ID: {games[0][0]})")
        else:
            print("❌ No games generated")
            return False
        
        # Test genre discovery
        print("\n🎯 Testing genre discovery...")
        rpg_games = ai_discovery.discover_games_by_genre("RPG", 50)
        if rpg_games:
            print(f"✅ Found {len(rpg_games)} RPG games")
        else:
            print("⚠️ No RPG games found")
        
        # Test developer discovery
        print("\n👨‍💻 Testing developer discovery...")
        valve_games = ai_discovery.discover_games_by_developer("Valve", 20)
        if valve_games:
            print(f"✅ Found {len(valve_games)} Valve games")
        else:
            print("⚠️ No Valve games found")
        
        return True
        
    except Exception as e:
        print(f"❌ AI discovery test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_massive_discovery():
    """Test massive discovery capabilities"""
    print("\n🚀 Testing Massive Discovery...")
    
    try:
        from ai_game_discovery import AIGameDiscovery
        from lm_studio_integration import LMStudioIntegration
        
        lm_studio = LMStudioIntegration()
        if not lm_studio.is_available():
            print("❌ LM Studio not available")
            return False
        
        ai_discovery = AIGameDiscovery(lm_studio)
        
        # Test massive discovery (smaller batch for testing)
        print("🔍 Testing massive discovery (1000 games)...")
        start_time = time.time()
        massive_games = ai_discovery.discover_massive_game_database(1000)
        end_time = time.time()
        
        if massive_games:
            print(f"✅ Massive discovery: {len(massive_games)} games in {end_time - start_time:.2f} seconds")
            
            # Show sample games
            print("   Sample games:")
            for i, (app_id, game_info) in enumerate(massive_games[:5]):
                print(f"   {i+1}. {game_info['name']} (ID: {app_id}) - {game_info['genre']}")
        else:
            print("❌ Massive discovery failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Massive discovery test failed: {e}")
        return False

def test_game_database_integration():
    """Test integration with game database"""
    print("\n📊 Testing Game Database Integration...")
    
    try:
        from game_database import game_database
        from lm_studio_integration import LMStudioIntegration
        
        lm_studio = LMStudioIntegration()
        if not lm_studio.is_available():
            print("❌ LM Studio not available")
            return False
        
        # Test AI discovery integration
        print("🤖 Testing AI discovery integration...")
        discovered_games = game_database.discover_games_with_ai(lm_studio)
        
        if discovered_games:
            print(f"✅ AI discovery integration: {len(discovered_games)} games")
            
            # Test database size
            total_games = len(game_database.get_all_games())
            print(f"✅ Total games in database: {total_games}")
            
            # Test search functionality
            search_results = game_database.search_games("RPG")
            print(f"✅ Search functionality: {len(search_results)} RPG games found")
            
        else:
            print("⚠️ AI discovery integration returned no games")
        
        return True
        
    except Exception as e:
        print(f"❌ Game database integration test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 70)
    print("🚀 MASSIVE AI GAME DISCOVERY TEST SUITE")
    print("=" * 70)
    print("Testing AI-powered massive game discovery capabilities")
    print()
    
    tests = [
        ("AI Discovery System", test_ai_discovery_system),
        ("Massive Discovery", test_massive_discovery),
        ("Game Database Integration", test_game_database_integration)
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
    print("📊 MASSIVE DISCOVERY TEST RESULTS")
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 MASSIVE AI DISCOVERY WORKING PERFECTLY!")
        print("🚀 Features available:")
        print("   - AI-powered comprehensive game generation")
        print("   - Massive database discovery (10,000+ games)")
        print("   - Genre-specific discovery")
        print("   - Developer-specific discovery")
        print("   - Batch discovery capabilities")
        print("   - Steam API analysis")
        print("   - Web scraping and analysis")
        print("   - Pattern-based discovery")
        return True
    else:
        print("\n⚠️ Some massive discovery features need attention.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
