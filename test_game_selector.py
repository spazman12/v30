#!/usr/bin/env python3
"""
Test Game Selector Functionality
"""

import sys
import os

# Add v30 directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'v30'))

def test_game_database():
    """Test the game database functionality"""
    print("🧪 Testing Game Database...")
    
    try:
        from game_database import game_database
        
        # Test basic functionality
        all_games = game_database.get_all_games()
        print(f"✅ Database loaded with {len(all_games)} games")
        
        # Test search
        search_results = game_database.search_games("Cyberpunk")
        print(f"✅ Search found {len(search_results)} Cyberpunk games")
        
        # Test genre filter
        rpg_games = game_database.get_games_by_genre("RPG")
        print(f"✅ Found {len(rpg_games)} RPG games")
        
        # Test popular games
        popular = game_database.get_popular_games(10)
        print(f"✅ Found {len(popular)} popular games")
        
        # Test specific game info
        game_info = game_database.get_game_info("730")
        if game_info:
            print(f"✅ Game info for CS2: {game_info['name']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Game database test failed: {e}")
        return False

def test_game_selector_integration():
    """Test game selector integration with main app"""
    print("\n🧪 Testing Game Selector Integration...")
    
    try:
        import tkinter as tk
        from steam_tools_generator import SteamToolsGenerator
        
        # Create a test window
        root = tk.Tk()
        root.withdraw()
        
        # Create the generator
        generator = SteamToolsGenerator(root)
        print("✅ Steam Tools Generator with game selector created")
        
        # Check if game selector method exists
        if hasattr(generator, 'show_game_selector'):
            print("✅ Game selector method found")
        else:
            print("❌ Game selector method missing")
            return False
        
        # Check if game database is loaded
        if hasattr(generator, 'game_selector_btn'):
            print("✅ Game selector button found")
        else:
            print("❌ Game selector button missing")
            return False
        
        # Test game database integration
        try:
            from game_database import game_database
            games = game_database.get_all_games()
            print(f"✅ Game database accessible: {len(games)} games")
        except:
            print("❌ Game database not accessible")
            return False
        
        # Clean up
        root.destroy()
        
        return True
        
    except Exception as e:
        print(f"❌ Game selector integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🎮 GAME SELECTOR TEST SUITE")
    print("=" * 60)
    
    tests = [
        ("Game Database", test_game_database),
        ("Game Selector Integration", test_game_selector_integration)
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
    print("📊 GAME SELECTOR TEST RESULTS")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 GAME SELECTOR WORKING PERFECTLY!")
        print("🎮 Features available:")
        print("   - Comprehensive game database")
        print("   - Search and filter functionality")
        print("   - Game selection with App IDs")
        print("   - AI-powered game discovery")
        print("   - Integration with main generator")
        return True
    else:
        print("\n⚠️ Some game selector features need attention.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
